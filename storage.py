import sqlite3
import time

DB = "data.db"

def init():
    conn = sqlite3.connect(DB)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        passed INTEGER,
        failed INTEGER
    )
    """)
    conn.close()

def save_run(passed, failed):
    conn = sqlite3.connect(DB)
    conn.execute(
        "INSERT INTO runs (timestamp, passed, failed) VALUES (?, ?, ?)",
        (time.strftime("%Y-%m-%d %H:%M:%S"), passed, failed)
    )
    conn.commit()
    conn.close()

def list_runs():
    conn = sqlite3.connect(DB)
    rows = conn.execute("SELECT * FROM runs ORDER BY id DESC").fetchall()
    conn.close()
    return rows