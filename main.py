from db_connection import create_connection

conn = create_connection()

if conn:
    conn.close()
    print("✅ Connection closed.")
