from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(database='amms.db')
 

	
def Home(app):
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
	       
	        if str(i[1]).startswith("6") or  str(i[1]).startswith("06"):
	            dataforgraph[0]+=1
	        elif str(i[1]).startswith("7") or  str(i[1]).startswith("07"):
	            dataforgraph[1]+=1
	        elif str(i[1]).startswith("8")  or str(i[1]).startswith("08"):
	            dataforgraph[2]+=1
	        elif str(i[1]).startswith("9") or  str(i[1]).startswith("09"):
	            dataforgraph[3]+=1
	        else:
	            dataforgraph[4]+=1
	    return render_template("index.html",subjects=subjects,logins=logins,late=all_student-logins,dataforgraph=dataforgraph)
