# 📚 Books & Authors Database Project

This project is part of **Module 5 (SQL & Python)**. It demonstrates how to design, create, and query a simple relational database using **SQLite**, **Python**, and **CSV** data files.

---

## ✅ Overview

We created a database called `book_db.sqlite` that contains two related tables:

- **authors**: Each record stores an author's unique ID, first name, and last name.
- **books**: Each record includes a book's ID, title, publication year, foreign key to author, and a `is_favorite` flag.

---

## 📂 Project Structure

datafun-05-sql/
│
├── books/
│ ├── create_tables.sql # SQL file to create the database schema
│ ├── create_tables.py # Python script to execute the SQL file
│ ├── insert_data.py # Python script to import CSV data
│ ├── query_data.py # Python script to query and display results
│ ├── book_db.sqlite # The actual SQLite database
│
├── data/
│ ├── authors.csv # CSV data for authors
│ ├── books.csv # CSV data for books

---

## 🧪 How to Use

To set up and run the project:

1. **Activate the virtual environment** (if not already):
   ```bash
   .\.venv\Scripts\Activate.ps1     # On Windows PowerShell

🛠 Technologies Used

Python 3.13

SQLite (via sqlite3 module)

CSV file processing (csv module)

VS Code

Git / GitHub for version control

📌 Notes
Data is loaded from CSV files stored in the data/ directory.

The foreign key relationship ensures that each book references a valid author.

The system prints clear logs to confirm each operation.

👨‍💻 Author
Sabri Hamdaoui
Northwest Missouri State University
Data Analytics - Module 5 Project


