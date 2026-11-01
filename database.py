import sqlite3


def init_db():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            email VARCHAR(50),
            password TEXT
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50),
            course VARCHAR(50)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR(50),
            department VARCHAR(50)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS academic_records (
            id INTEGER PRIMARY KEY,
            name VARCHAR(50),
            course VARCHAR(50),
            marks INTEGER,
            grade VARCHAR(10)
        )
    """)

    cursor.execute(
        "INSERT OR IGNORE INTO users (id, email, password) VALUES (1, ?, ?)",
        ("example@gmail.com", "12345")
    )

    connection.commit()
    connection.close()


init_db()