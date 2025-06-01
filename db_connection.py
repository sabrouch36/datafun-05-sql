import sqlite3
from pathlib import Path

DB_NAME = "datafun.db"
DB_PATH = Path(__file__).parent / DB_NAME

def create_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        print(f"✅ Connected to database at {DB_PATH}")
        return conn
    except sqlite3.Error as e:
        print(f"❌ Error: {e}")
        return None
