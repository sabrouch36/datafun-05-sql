import sqlite3
from pathlib import Path

def run_select_query(sql_file_path):
    """Run a SELECT query from a .sql file and display the results."""
    db_path = Path(__file__).parent / "datafun.db"
    sql_path = Path(sql_file_path)

    if not sql_path.exists():
        print(f"❌ SQL file not found: {sql_path}")
        return

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        with open(sql_path, 'r', encoding='utf-8') as file:
            query = file.read()
            cursor.execute(query)
            results = cursor.fetchall()

            print("✅ Query Results:")
            for row in results:
                print(row)

if __name__ == "__main__":
    run_select_query("sql_queries/select_customers.sql")
