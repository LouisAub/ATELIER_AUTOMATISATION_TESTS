import requests
import time
import sqlite3
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# ================= DATABASE =================
def init_db():
    conn = sqlite3.connect("data.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        latency REAL,
        status TEXT
    )
    """)
    conn.close()

init_db()

# ================= HOME =================
@app.get("/")
def home():
    return render_template("consignes.html")

# ================= API TEST =================
API_URL = "https://api.ipify.org?format=json"

def run_test():
    start = time.time()

    try:
        response = requests.get(API_URL, timeout=3)
        latency = (time.time() - start) * 1000

        data = response.json()

        if response.status_code == 200 and "ip" in data:
            status = "PASS"
        else:
            status = "FAIL"

    except Exception:
        latency = 0
        status = "ERROR"

    conn = sqlite3.connect("data.db")
    conn.execute(
        "INSERT INTO runs (timestamp, latency, status) VALUES (?, ?, ?)",
        (time.strftime("%Y-%m-%d %H:%M:%S"), latency, status)
    )
    conn.commit()
    conn.close()

    return {
        "status": status,
        "latency_ms": round(latency, 2)
    }

# ================= RUN =================
@app.route("/run")
def run():
    return jsonify(run_test())

# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    conn = sqlite3.connect("data.db")
    rows = conn.execute("SELECT * FROM runs ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("dashboard.html", rows=rows)

# ================= MAIN =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)