import sqlite3
import pandas as pd

def fetch_data_from_database():


    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()


    cursor.execute("DROP TABLE IF EXISTS users")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
    """)


    users_to_insert = [
        ('John', 25),
        ('Bob', 30),
        ('Alice', 22),
        ('David', 28),
        ('Emma', 24)
    ]
    cursor.executemany("INSERT INTO users (name, age) VALUES (?, ?)", users_to_insert)


    conn.commit()


    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()


    df = pd.DataFrame(rows, columns=['id', 'name', 'age'])



    df['marks'] = [78, 85, 67, 90, 88]


    print("Original DataFrame:\n")
    print(df)


    sorted_df = df.sort_values(by='age')

    print("\nSorted by Age:\n")
    print(sorted_df)


    mean_marks = df['marks'].mean()

    print("\nMean Marks:", mean_marks)


    above_mean = df[df['marks'] > mean_marks]

    print("\nStudents scoring above mean:\n")
    print(above_mean)


    conn.close()

fetch_data_from_database()
