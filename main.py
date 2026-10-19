import sqlite3

db = sqlite3.connect("students.db")
c = db.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT,
    email TEXT
)""")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        age = int(input("Age: "))
        course = input("Course: ")
        email = input("Email: ")

        c.execute(
            "INSERT INTO students (name, age, course, email) VALUES (?, ?, ?, ?)",
            (name, age, course, email)
        )
        db.commit()
        print("Student added!")

    elif choice == "2":
        c.execute("SELECT * FROM students")
        for student in c.fetchall():
            print(student)

    elif choice == "3":
        sid = input("Enter student ID: ")
        c.execute("SELECT * FROM students WHERE id = ?", (sid,))
        print(c.fetchone() or "Student not found!")

    elif choice == "4":
        sid = input("Enter student ID to delete: ")
        c.execute("DELETE FROM students WHERE id = ?", (sid,))
        db.commit()
        print("Student deleted if the ID existed.")

    elif choice == "5":
        break

    else:
        print("Invalid choice!")

db.close()