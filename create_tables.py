import sqlite3
from pathlib import Path

def run_sql_script(sql_file_path):
    """Execute a SQL script from a .sql file."""
    db_path = Path(__file__).parent / "datafun.db"
    sql_path = Path(sql_file_path)

    if not sql_path.exists():
        print(f"❌ SQL file not found: {sql_path}")
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        with open(sql_path, 'r', encoding='utf-8') as file:
            sql_script = file.read()
            cursor.executescript(sql_script)
            print(f"✅ Successfully executed SQL script: {sql_file_path}")

if __name__ == "__main__":
    run_sql_script("sql_create/create_customers.sql")
