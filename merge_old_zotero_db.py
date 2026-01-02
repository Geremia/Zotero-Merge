#!/usr/bin/env python3

# based on: https://chatgpt.com/share/6958136b-3a38-8011-9c1c-960a3aaa993f

import sys
import sqlite3

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <current_db> <backup_db>")
    sys.exit(1)

current_db = sys.argv[1]
backup_db = sys.argv[2]

conn = sqlite3.connect(current_db)
conn.execute(f"ATTACH DATABASE '{backup_db}' AS backup_db;")

tables = conn.execute('''
SELECT 
    name
FROM 
    sqlite_schema
WHERE 
    type ='table'
ORDER by name
''').fetchall()

for (t,) in tables:
    sql = f'INSERT OR IGNORE INTO "{t}" SELECT * FROM backup_db."{t}"'
    print(sql)
    conn.execute(sql)

conn.commit()
conn.close()

