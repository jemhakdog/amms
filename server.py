from flask import  Flask,render_template


from routes.home import  Home
from routes.attendance import  Attendance
from routes.manage import  Manage
from  routes.login import Login
from routes.student import Student
app=Flask("attendanceMs")

Home(app)
Manage(app)
Attendance(app)
Login(app)
Student(app)
@app.route("/")
def login_faculty():
    yield "hahahss"


