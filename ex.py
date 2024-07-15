import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect("amms.db")
cursor = conn.cursor()
cursor.execute("""
    DROP TABLE subject
""")
# Create tables
cursor.execute("""
    CREATE TABLE IF NOT EXISTS subject (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        code TEXT NOT NULL,
        start_time TIME,
        end_time TIME
    );
""")
# cursor.execute("""
#     DROP TABLE attendance_log
# """)
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS attendance_log (
#         id INTEGER,
#         time TIME,
#         name varchar,
#         date DATE
#     );
# """)
    
cursor.execute("""
    DROP TABLE students
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        middle_initial TEXT,
        last_name TEXT NOT NULL,
        gender TEXT NOT NULL,
        student_id TEXT NOT NULL
    );
""")
cursor.execute("""
    DROP TABLE faculty
""")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS faculty (
        id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL,
        type TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        subject_id INTEGER,
        student_id INTEGER,
        teacher TEXT,
        FOREIGN KEY (subject_id) REFERENCES subjects (id),
        FOREIGN KEY (student_id) REFERENCES students (id)
    );
""")

# Insert subjects
subjects = [
    ("Mathematics", "MATH101",'7:00','8:00'),
    ("Science", "SCI102",'8:00','9:00' ),
    ("English", "ENG103",'10:00','11:00'),
    ("History", "HIS104",'1:00','2:00'),
    ("Geography", "GEO105",'2:00','3:00'),
    ("Computer Science", "CS106",'3:00','4:00'),
    ("Physics", "PHY107",'4:00','5:00'),
]

cursor.executemany("INSERT INTO subject (name, code,start_time,end_time) VALUES (?,?,?,?)", subjects)

# Insert students
students = [
    ("John", "A", "Doe", "Male", "S101"),
    ("Jane", "B", "Smith", "Female", "S102"),
    ("Bob", "C", "Johnson", "Male", "S103"),
    ("Alice", "D", "Williams", "Female", "S104"),
    ("Mike", "E", "Brown", "Male", "S105"),
    ("Emily", "F", "Davis", "Female", "S106"),
    ("Tom", "G", "Miller", "Male", "S107"),
    ("Sarah", "H", "Wilson", "Female", "S108"),
    ("David", "I", "Moore", "Male", "S109"),
    ("Rebecca", "J", "Taylor", "Female", "S110")
]

cursor.executemany("INSERT INTO students (first_name, middle_initial, last_name, gender, student_id) VALUES (?,?,?,?,?)", students)

# Insert faculty
faculty = [
    ("John", "Doe", "johndoe@example.com", "teacher"),
    ("Jane", "Smith", "janesmith@example.com", "teacher"),
]

cursor.executemany("INSERT INTO faculty (first_name, last_name, email, type) VALUES (?,?,?,?)", faculty)

# Commit changes
conn.commit()

# Close the connection

conn.close()

