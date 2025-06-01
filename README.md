# datafun-05-sql

## Overview
This project demonstrates how to use Python and SQL (SQLite) to create, populate, and query a relational database. It is part of the CC5.2 module for learning file-based relational databases and basic data manipulation.

## Project Structure
datafun-05-sql/
├── data/ # Placeholder for CSV files
├── sql_create/ # SQL scripts for table creation
├── sql_insert/ # SQL scripts for inserting data
├── sql_queries/ # SQL scripts for querying data
├── db_connection.py # Handles SQLite connection
├── create_tables.py # Executes table creation SQL
├── insert_data.py # Executes data insertion SQL
├── query_data.py # Executes SELECT queries and displays results
├── main.py # Tests database connection
├── requirements.txt # Python package requirements
└── README.md # Project documentation


## Setup Instructions

### 1. Create and activate virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows

##2. Install dependencies

pip install pandas
pip freeze > requirements.txt

###3-Execution Commands

python create_tables.py     # Create 'customers' table
python insert_data.py       # Insert sample customer data
python query_data.py        # Query and display data from 'customers'

## Output Example ##

✅ Query Results:
(1, 'Alice', 'Johnson', 'alice.johnson@example.com', '2024-11-01')
(2, 'Bob', 'Smith', 'bob.smith@example.com', '2024-12-15')
(3, 'Charlie', 'Lee', 'charlie.lee@example.com', '2025-01-10')
