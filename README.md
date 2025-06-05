# 📘 DataFun-05-SQL Project

## 🧠 Project Overview

This project demonstrates core SQL and Python skills for working with relational databases using `SQLite`. It includes creating a database, defining tables, inserting records, and querying data using both SQL files and Python scripts.

---

## 📂 Project Structure

datafun-05-sql/
│
├── book_db.sqlite # SQLite database file
├── create_tables.py # Python script to create tables
├── insert_data.py # Python script to insert data
├── query_data.py # Python script to run SQL SELECT queries
├── sql_create/
│ └── create_tables.sql # SQL file with table creation
├── sql_insert/
│ └── insert_records.sql # SQL file to insert authors and books
├── sql_queries/
│ ├── select_books.sql
│ ├── select_books_ordered.sql
│ ├── select_books_after_1950.sql
│ ├── select_books_with_authors.sql
│ ├── select_authors_distinct.sql
│ ├── update_author_name.sql
│ └── delete_book_by_title.sql
├── data/
│ ├── authors.csv
│ └── books.csv
└── README.md


---

## ✅ Skills Demonstrated

- ✔ Create a SQLite database using Python
- ✔ Create tables with foreign key relationships
- ✔ Insert data via SQL scripts
- ✔ Read and display records using `SELECT`
- ✔ Use `WHERE` to filter records
- ✔ Use `ORDER BY` to sort records
- ✔ Use `JOIN` to combine related tables
- ✔ Use `DISTINCT` to remove duplicates
- ✔ Update data using `UPDATE`
- ✔ Delete records using `DELETE`

---

## 💡 Sample SQL Queries Used

```sql
-- Select all books
SELECT * FROM books;

-- Select books after 1950
SELECT * FROM books WHERE year_published > 1950;

-- Order books by year descending
SELECT * FROM books ORDER BY year_published DESC;

-- Join books with authors
SELECT books.title, authors.first, authors.last
FROM books
INNER JOIN authors ON books.author_id = authors.author_id;

-- Update author name
UPDATE authors SET first = 'Nelle' WHERE last = 'Lee';

-- Delete a specific book
DELETE FROM books WHERE title = '1984';

🧪 How to Run
From the project root folder, in your terminal:

# Create database and tables
python create_tables.py

# Insert records into tables
python insert_data.py

# Run SELECT queries
python query_data.py

✍️ Author
Sabri Hamdaoui – Data Analytics Student
Module 5 – SQL Fundamentals
Northwest Missouri State University

