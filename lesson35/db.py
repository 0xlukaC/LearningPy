#!/home/lukachalker/myenv/bin/python3

import sqlite3

conn = sqlite3.connect("school.db")
curs = conn.cursor()
curs.execute(
    """CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY UNIQUE, 
name TEXT UNIQUE,
age INTEGER)
"""
)


def addguy(name: str, age: int):
    try:
        curs.execute(
            "INSERT OR IGNORE INTO students (name, age) VALUES (?, ?)", (name, age)
        )
    except sqlite3.IntegrityError:
        ...


addguy("Alice", 16)
addguy("Goge", 120)
addguy("Stew", 1)
addguy("kelp", 16)

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

print("\nage > 15")
for row in curs.execute("SELECT name FROM students WHERE age > 15"):
    print(row)

print("\nalphabetical order")
for row in curs.execute("SELECT * FROM students ORDER BY name ASC"):
    print(row)

print("\nGroup by same name")
for row in curs.execute("SELECT age, COUNT(*) FROM students GROUP BY age"):
    print(f"Age: {row[0]}, Students: {row[1]}")
# groups rows with the same value into one row

curs.execute("SELECT COUNT(*) FROM students")
count = curs.fetchone()[0]
print(f"\nNumber of entries: {count}")
conn.commit()
curs.close()
conn.close()
