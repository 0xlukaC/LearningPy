#!/home/lukachalker/myenv/bin/python3

import sqlite3

conn = None  # it will say conn is possibly unbound so you need to set it before the trycatch
try:

    conn = sqlite3.connect("school.db")
    curs = conn.cursor()
    curs.execute(
        """CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY UNIQUE, 
    name TEXT UNIQUE,
    grade REAL)
    """
    )

    def addguy(name: str, grade: float):
        try:
            curs.execute(
                "INSERT OR IGNORE INTO students (name, grade) VALUES (?, ?)",
                (name, grade),
            )
        except sqlite3.IntegrityError:
            ...

    addguy("Alice", 16)
    addguy("Goge", 90)
    addguy("Stew", 1)
    addguy("kelp", 80)

    # curs.execute(
    #     """DELETE FROM students WHERE id NOT IN (
    #     SELECT MIN(id)
    #     FROM students
    #     GROUP BY name)
    #     """
    # )

    # curs.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Alice", 16))
    print("everything")
    for row in curs.execute("SELECT * FROM students"):
        print(row)

    def passed():
        print("\ngrade > 85")
        for row in curs.execute("SELECT * FROM students WHERE grade > 85"):
            print(f"Grade: {row[2]}, Name: {row[1]}")

    passed()

    curs.execute("SELECT COUNT(*) FROM students")
    count = curs.fetchone()[0]
    print(f"\nNumber of entries: {count}")
    conn.commit()
    curs.close()

except sqlite3.OperationalError as e:
    print("operationalerr", e)  # errors that are related to the database’s operation
except sqlite3.ProgrammingError as e:
    print("programmingErr", e)  # errors that are related to the programmers operation
finally:
    if conn:
        conn.close()
