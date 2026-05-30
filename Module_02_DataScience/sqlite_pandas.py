import sqlite3
import pandas as pd

def fetch_data_from_database():
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users
    (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)
    """)

    cursor.execute("INSERT INTO users (name, age) VALUES ('Jhon', 25)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Alice', 22)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('David', 28)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Emma', 24)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Bob', 30)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Michael', 27)")
    cursor.execute("INSERT INTO users (name, age) VALUES ('Sophia', 21)")

    conn.commit()

    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    df = pd.DataFrame(rows, columns=['id', 'name', 'age'])
    print(df)

    conn.close()

fetch_data_from_database()