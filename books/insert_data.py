import sqlite3
import csv
from pathlib import Path

db_path = Path(__file__).parent / "book_db.sqlite"
authors_csv = Path(__file__).parent.parent / "data" / "authors.csv"
books_csv = Path(__file__).parent.parent / "data" / "books.csv"

def insert_authors():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        with open(authors_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            authors = [(row["author_id"], row["first"], row["last"]) for row in reader]
        cursor.executemany(
            "INSERT INTO authors (author_id, first, last) VALUES (?, ?, ?)", authors)
        print("✅ Authors inserted.")

def insert_books():
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        with open(books_csv, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            books = [(row["book_id"], row["title"], int(row["year_published"]), row["author_id"]) for row in reader]
        cursor.executemany(
            "INSERT INTO books (book_id, title, year_published, author_id) VALUES (?, ?, ?, ?)", books)
        print("✅ Books inserted.")

if __name__ == "__main__":
    insert_authors()
    insert_books()
