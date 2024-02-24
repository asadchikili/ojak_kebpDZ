import sqlite3

conn = sqlite3.connect('ojak_kebab.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        date_joined TEXT
    )
''')

conn.commit()
conn.close()
