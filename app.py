from flask import Flask, render_template, request, redirect
import sqlite3
from database import init_db

app = Flask(__name__)
init_db()

@app.route("/")
def home():
    return render_template("login.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=? AND password=?",
            (email, password)
        )

        user = cursor.fetchone()
        connection.close()

        if user:
            return redirect("/dashboard")
        else:
            return "Invalid email or password"

    return render_template("login.html")




@app.route("/dashboard")
def dashboard():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM students")
    student_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM courses")
    course_count = cursor.fetchone()[0]

    connection.close()

    return render_template(
        "dashboard.html",
        student_count=student_count,
        course_count=course_count
    )

@app.route("/students")
def students():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    connection.close()

    return render_template("students.html", students=students)

@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        course = request.form["course"]

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )

        connection.commit()
        connection.close()

        return redirect("/students")

    return render_template("add_student.html")

@app.route("/courses")
def courses():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM courses")
    courses = cursor.fetchall()

    connection.close()

    return render_template("courses.html", courses=courses)

@app.route("/courses/add", methods=["GET", "POST"])
def add_course():
    if request.method == "POST":
        course_name = request.form["course"]
        department = request.form["department"]

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO courses (course_name, department) VALUES (?, ?)",
            (course_name, department)
        )

        connection.commit()
        connection.close()

        return redirect("/courses")

    return render_template("add_course.html")

@app.route("/academics")
def academic():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM academic_records")
    records = cursor.fetchall()

    connection.close()

    return render_template("academic.html", records=records)

@app.route("/academics/add", methods=["GET", "POST"])
def add_accademic():
    if request.method == "POST":
        name = request.form["name"]
        course = request.form["course"]
        marks = request.form["marks"]
        grade = request.form["grade"]

        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO academic_records (name, course, marks, grade) VALUES (?, ?, ?, ?)",
            (name, course, marks, grade)
        )

        connection.commit()
        connection.close()

        return redirect("/academics")

    return render_template("add_academic.html")

@app.route("/academics/delete/<int:id>")
def delete_academic(id):
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM academic_records WHERE id=?",
        (id,)
    )

    connection.commit()
    connection.close()

    return redirect("/academics")
if __name__ == "__main__":
 app.run(debug=True)