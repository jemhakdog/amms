from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(host='localhost', database='amms.db', user='root', password='')

app=Flask("attendanceMs")


@app.route("/")
def home():
    db= getdatabase()
    subjects = db.retrieve_table('subject')
    todays_attendance=db.retrieve_todays_attendance("attendance_log", date=str(datetime.datetime.today()).split(" ")[0]
)   
    studens=db.retrieve_table("students")
    all_student=len(studens)
    logins=len(todays_attendance)
    db.close()
    dataforgraph=[0,0,0,0,0]
    for i in todays_attendance:
        print(i[1])
        if str(i[1]).startswith("6"):
            dataforgraph[0]+=1
        elif str(i[1]).startswith("7"):
            dataforgraph[1]+=1
        elif str(i[1]).startswith("8"):
            dataforgraph[2]+=1
        elif str(i[1]).startswith("9"):
            dataforgraph[3]+=1
        else:
            dataforgraph[4]+=1
    return render_template("index.html",subjects=subjects,logins=logins,late=all_student-logins,dataforgraph=dataforgraph)


@app.route("/attendance",methods=["GET","POST"])
def attendance():
    db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
    now = datetime.datetime.now()
    time = now.strftime("%I:%M %p")
    #time = '8:00 AM'
    if request.method=="GET":
        todays_attendance=db.retrieve_todays_attendance("attendance_log", date=str(datetime.datetime.today()).split(" ")[0]
)
        db.close()
        return render_template("attendance.html",name="",sex="",type="",id="",didsomeonelogin=False,todays_attendance=todays_attendance)
    elif request.method=="POST":
        id=request.form.get("studentid")
        try:
            student = db.retrieve_id('students',int(id))
            print(student)
        except e as Exception:
           
            todays_attendance=db.retrieve_todays_attendance("attendance_log", date=str(datetime.datetime.today()).split(" ")[0])
            return render_template("attendance.html",name="",sex="",type="",id="",didsomeonelogin=False,todays_attendance=todays_attendance)

        if request.form:
            if student:
                name=student[1]+' '+student[2]+' '+student[3]
                date=str(datetime.datetime.today()).split(" ")[0]
                isexisting=db.rsa("attendance_log",id,date)
                if isexisting:

                    todays_attendance=db.retrieve_todays_attendance("attendance_log",date)
                    return render_template("attendance.html",name="",sex="",type="",id="",todays_attendance=todays_attendance,didsomeonelogin=False)
                value=(id,name,time,date)
                db.insert_to_attendance_log(value)
                todays_attendance=db.retrieve_todays_attendance("attendance_log",date)
                db.close()
                return render_template("attendance.html",student=student,todays_attendance=todays_attendance,time=time,didsomeonelogin=True)
        todays_attendance=db.retrieve_todays_attendance("attendance_log", date=str(datetime.datetime.today()).split(" ")[0]
)
        db.close()
        return render_template("attendance.html",name="",sex="",type="",id="",todays_attendance=todays_attendance,didsomeonelogin=False)


@app.route("/manage")
def manage():
    db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
    students_table = db.retrieve_table('students')
    db.close()
    return render_template("manage.html",students=students_table)
@app.route("/manage/update_and_insert",methods=["post","POST"])
def update_student():
    if request.method=="POST":
        fname=request.form.get("fname")
        mname=request.form.get("mname")
        lname=request.form.get("lname")
        id=request.form.get("student_id")
        gender=request.form.get("gender")
        operation=request.form.get("operation")
        if request.form.get("isedit") and not operation:
            db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
            db.execute(f"UPDATE `students` SET `first_name`='{fname}', `middle_initial`='{mname}',`last_name`='{lname}',`gender`='{gender}',`id`='{id}' WHERE `id`='{id}'")
            db.close()
        elif request.form.get("operation"):
            print("delete")
            db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
            db.execute(f"DELETE FROM `students` WHERE `id`='{id}'")
            db.execute(f"DELETE FROM `attendance_log` WHERE `id`='{id}'")
            db.close()
        else:
            db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
            values=(fname,lname,mname,gender,id)
            db.execute(f"INSERT INTO `students`(`first_name`, `last_name`, `middle_initial`, `gender`, `id`) VALUES  {values}")
            db.close()

    return redirect("/manage")
@app.route('/manage/subjects')
def manage_subjects():
    db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
    subjects = db.retrieve_table('subject')
    return render_template("manage_subjects.html",subjects=subjects)
@app.route('/manage/teachers')
def manage_teachers():
    db = MySQLDatabase(host='localhost', database='amms.db', user='root', password='')
    faculty = db.retrieve_table('faculty')
    return render_template("manage_teachers.html",faculty=faculty)

@app.route("/login")
def login():
    return render_template("login.html")

app.run(debug=True)