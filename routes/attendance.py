from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(database='amms.db')
 
def Attendance(app):
	@app.route("/attendance",methods=["GET","POST"])
	def attendance():
	    db = getdatabase()
	    now = datetime.datetime.now()
	    time = now.strftime("%I:%M %p")
	    #time = '9:00 AM'
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
	        except:
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