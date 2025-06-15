#!/home/lukachalker/myenv/bin/python3

import sqlite3

conn = sqlite3.connect("school.db")
curs = conn.cursor()
curs.execute(
    """CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY UNIQUE, 
name TEXT UNIQUE,
lastname TEXT,
age DATE,
course_id INTEGER,
FOREIGN KEY (course_id) REFERENCES courses(id)
)
"""
)

curs.execute(
    """
    CREATE TABLE IF NOT EXISTS courses (
    id INTEGER PRIMARY KEY UNIQUE,
    courseName TEXT UNIQUE
    )
    """
)


def addguy(name: str, lastname: str, age: str, course: str):
    try:
        course_id = None
        if course:
            curs.execute(
                "INSERT OR IGNORE INTO courses (courseName) VALUES (?)", (course,)
            )
            curs.execute("SELECT id FROM courses WHERE courseName = ?", (course,))
            course_id = curs.fetchone()[0]

        curs.execute(
            "INSERT OR IGNORE INTO students (name, lastname, age, course_id) VALUES (?, ?, ?, ?)",
            (name, lastname, age, course_id),
        )
    except sqlite3.IntegrityError:
        ...


addguy("Alice", "mace", "2007-02-01", "math")
addguy("Goge", "ng", "2000-01-30", "english")
addguy("Jenavieve", "vavance", "1000-07-28", "hass")
addguy("kelp", "Celp", "2008-03-06", "science")

# curs.execute(
#     """DELETE FROM students WHERE id NOT IN (
#     SELECT MIN(id)
#     FROM students
#     GROUP BY name)
#     """
# )

# curs.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 16))
print("everything")
for row in curs.execute("SELECT * FROM students"):
    print(row)

curs.execute("SELECT COUNT(*) FROM students")
count = curs.fetchone()[0]
print(f"\nNumber of entries: {count}")
conn.commit()
curs.close()
conn.close()
