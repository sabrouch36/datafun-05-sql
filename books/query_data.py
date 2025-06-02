import sqlite3
from pathlib import Path

db_path = Path(__file__).parent / "book_db.sqlite"

def show_all_authors():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        rows = cursor.fetchall()
        print("\n📚 Authors:")
        for row in rows:
            print(row)

def show_all_books():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT books.title, books.year_published, authors.first || ' ' || authors.last AS author_name
            FROM books
            JOIN authors ON books.author_id = authors.author_id
        """)
        rows = cursor.fetchall()
        print("\n📖 Books with Authors:")
        for row in rows:
            print(row)

if __name__ == "__main__":
    show_all_authors()
    show_all_books()
