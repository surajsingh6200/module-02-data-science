import sqlite3
conn = sqlite3.connect("example.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
)
""")


cur.execute("""
CREATE TABLE IF NOT EXISTS faculty(
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT,
    salary INTEGER
)
""")


cur.execute("DELETE FROM students")
cur.execute("DELETE FROM faculty")


students = [
    ("Rahul", "Python"),
    ("Aman", "Python"),
    ("Priya", "Java"),
    ("Riya", "Java"),
    ("Karan", "SQL")
]

cur.executemany(
    "INSERT INTO students(name, subject) VALUES (?, ?)",
    students
)


faculty = [
    ("Mr Sharma", "Python", 50000),
    ("Mr Gupta", "Java", 55000),
    ("Mr Singh", "SQL", 45000)
]

cur.executemany(
    "INSERT INTO faculty(name, subject, salary) VALUES (?, ?, ?)",
    faculty
)

conn.commit()

print("\n--- STUDENT WITH FACULTY ---\n")

cur.execute("""
SELECT s.name,
       s.subject,
       f.name,
       f.salary
FROM students s
JOIN faculty f
ON s.subject = f.subject
""")

rows = cur.fetchall()

for row in rows:
    print(row)

print("\n--- FACULTY STUDENT COUNT & REVENUE ---\n")

cur.execute("""
SELECT f.name,
       f.subject,
       COUNT(s.id) AS total_students,
       COUNT(s.id) * 500 AS total_fee,
       f.salary
FROM faculty f
LEFT JOIN students s
ON f.subject = s.subject
GROUP BY f.subject
""")

rows = cur.fetchall()

for row in rows:
    print(row)

conn.close()