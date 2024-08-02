import sqlite3
import time

def init_db():
    conn = sqlite3.connect('document_usage.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS access_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        document_id TEXT,
        action TEXT,
        timestamp REAL
    )
    ''')
    conn.commit()
    conn.close()

def log_document_access(user_id, document_id, action):
    conn = sqlite3.connect('document_usage.db')
    cursor = conn.cursor()
    timestamp = time.time()
    cursor.execute("INSERT INTO access_logs (user_id, document_id, action, timestamp) VALUES (?, ?, ?, ?)",
                   (user_id, document_id, action, timestamp))
    conn.commit()
    conn.close()
