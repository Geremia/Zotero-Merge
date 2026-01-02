#!/usr/bin/env python3

# 🎩-tip: https://chatgpt.com/share/69580fb7-d048-8011-a819-fabaa5ced1a0

import sys
import sqlite3

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <sqlite_db>")
    sys.exit(1)

db = sys.argv[1]

conn = sqlite3.connect(db)
cur = conn.cursor()

cur.execute("""
SELECT name FROM sqlite_master
WHERE type='table' AND name NOT LIKE 'sqlite_%';
""")

for (table,) in cur.fetchall():
    cur.execute(f'SELECT COUNT(*) FROM "{table}"')
    count = cur.fetchone()[0]
    print(f"{table:>24}: {count}")

conn.close()
