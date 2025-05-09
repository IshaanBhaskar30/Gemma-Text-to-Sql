import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# --- Streamlit App Configuration ---
st.set_page_config(page_title="SQL Query Generator")
st.title("Gemini App to Retrieve SQL Data")

# --- Sidebar for API Key Input ---
with st.sidebar:
    st.header("🔐 API Key Configuration")
    user_api_key = st.text_input("Enter your Google API Key", type="password")

# --- Prompt Template ---
prompt = [
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS.

    Example 1 - How many entries of records are present?  
    SQL: SELECT COUNT(*) FROM STUDENT;

    Example 2 - Tell me all the students studying in Data Science class?  
    SQL: SELECT * FROM STUDENT WHERE CLASS="Data Science";

    Return only SQL code without markdown, backticks, or extra explanation.
    """
]

# --- Function to Get Gemini Response (SQL Query) ---
def get_gemini_response(question, prompt, api_key):
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    response = model.generate_content([prompt[0], question])
    return response.text.strip()

# --- Function to Execute SQL Query ---
def read_sql_query(sql, db_path):
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        return [("Error", str(e))]

# --- Main Input ---
question = st.text_input("Ask your question in plain English:")

if st.button("Submit"):
    if not user_api_key:
        st.error("Please enter your Google API key in the sidebar.")
    elif not question:
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating SQL and fetching data..."):
            sql_query = get_gemini_response(question, prompt, user_api_key)
            st.code(sql_query, language="sql")

            data = read_sql_query(sql_query, "student.db")
            st.subheader("📊 Query Results")
            if data:
                for row in data:
                    st.write(row)
            else:
                st.info("No results returned.")
