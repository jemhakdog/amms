from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(database='amms.db')
 
 


def Manage(app):
	@app.route("/manage")
	def manage():
	    db = getdatabase()
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
	            db = getdatabase()
	            db.execute(f"UPDATE `students` SET `first_name`='{fname}', `middle_initial`='{mname}',`last_name`='{lname}',`gender`='{gender}',`id`='{id}' WHERE `id`='{id}'")
	            db.close()
	        elif request.form.get("operation"):
	            print("delete")
	            db = getdatabase()
	            db.execute(f"DELETE FROM `students` WHERE `id`='{id}'")
	            db.execute(f"DELETE FROM `attendance_log` WHERE `id`='{id}'")
	            db.close()
	        else:
	            db =getdatabase()
	            values=(fname,lname,mname,gender,id)
	            db.execute(f"INSERT INTO `students`(`first_name`, `last_name`, `middle_initial`, `gender`, `id`) VALUES  {values}")
	            db.close()
	
	    return redirect("/manage")
	@app.route('/manage/subjects')
	def manage_subjects():
		db =getdatabase()
		subjects = db.retrieve_table('subject')
		return render_template("manage_subjects.html",subjects=subjects)
	@app.route('/manage/teachers')
	def manage_teachers():
	    db =getdatabase()
	    faculty = db.retrieve_table('faculty')
	    return render_template("manage_teachers.html",faculty=faculty)