🧠 Natural Language to SQL Query Generator using Gemini

📘 Project Overview

This project is a Streamlit-based application that allows users to ask natural language questions about a student database. The app uses Google's Gemini (1.5 Flash) model to convert English questions into valid SQL queries, which are then executed against a local SQLite database. The goal is to make SQL querying accessible for non-technical users.

🔍 Key Features

->🤖 Converts plain English questions into accurate SQL queries using Gemini.

->🗄️ Interacts with a sample SQLite database (student.db) containing student records.

->🔐 Securely input your Google API key in the sidebar.

->💬 View both the generated SQL query and the executed result.

🧠 How It Works

->A user types a natural language question like:

    "Which students are in section A?"

->The app sends the question and a structured prompt to the Gemini 1.5 Flash model.

->Gemini returns a valid SQL query
->The query is executed against the student.db database, and results are displayed in the app.

The database contains student-related information such as names, class names, section, and marks. Users can ask questions like “How many students are in Data Science?”, “Show students who scored more than 80 marks”, or “List all entries in the table”, and the app will automatically generate the corresponding SQL command, execute it, and display the results.

🖼️ UI Overview

->Sidebar:

    o Input field for your Google API key.

->Main Panel:

    o Ask any English question about the student database.

    o See the generated SQL query.

    o View the query result table.

