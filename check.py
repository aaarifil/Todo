# ...existing code...
import sqlite3
from pathlib import Path

db = Path("dev.db")
if not db.exists():
    print("dev.db not found:", db.resolve())
    raise SystemExit(1)

conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cur.fetchall())

cur.execute("SELECT id, title, description, is_done, created_at, updated_at FROM todos LIMIT 20;")
for row in cur.fetchall():
    print(row)
conn.close()
# ...existing code...