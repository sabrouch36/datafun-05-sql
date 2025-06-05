import sqlite3
import pathlib

# Path to the database and SQL file
db_file = pathlib.Path("book_db.sqlite")
sql_file = pathlib.Path("sql_insert", "insert_records.sql")

def insert_data():
    """Execute SQL script to insert records into the database."""
    try:
        with sqlite3.connect(db_file) as conn:
            with open(sql_file, "r") as file:
                sql_script = file.read()
            conn.executescript(sql_script)
            print("✅ Data inserted successfully.")
    except sqlite3.Error as e:
        print("❌ Error inserting data:", e)

if __name__ == "__main__":
    insert_data()
