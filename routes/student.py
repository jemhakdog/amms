
from flask import *
import datetime
import webbrowser

from manage_database import MySQLDatabase


def getdatabase():
	return MySQLDatabase(database='amms.db')


def attendance_time_checker(time1):
    if not time1:
        time1 = '0000'
    db = getdatabase()
    subjects = db.retrieve_table('subject')
    todays_attendance = db.retrieve_todays_attendance('attendance_log',
            date=str(datetime.datetime.today()).split(' ')[0])
    subs = []
    present = False
    isabsent = False
    for i in subjects:
        a = list(i)
        timee = a[3][0]
        if time1[0] == '0':
            time2 = time1[1]    
        else:
            time2 = time1[0]     
        if (timee == time2 and not time1[3] == ':')   or present or time2==a[4][0]:
            if not isabsent:
                time3 = time1.split(':')[1].split(' ')[0]
            else:
                time3 = '00'
            if int(time3) <= 10 :
                a.append('present')
                subs.append(a)
                present = True
            elif int(time3) >= 10 and int(time3) <= 40:
                a.append('late')
                subs.append(a)
                isabsent = True
                present = True
            elif int(time3) >= 40 :
                a.append('absent')
                subs.append(a)
                present = True
                isabsent=True
        else:
            a.append('absent')
            subs.append(a)
    return subs

def r_home(id):
		resp = redirect(url_for('student_home'))
		resp.set_cookie('student_id', id)
		return resp
def Student(app):
	@app.route('/login/student', methods=['GET', 'POST'])
	def student_login():
		if request.method == 'POST':
			id = request.form.get('id')
			password = request.form.get('password')
			db = getdatabase()
			students = db.retrieve_table('students')
			for student in students:
				if int(id) == int(student[0]):
					print("logging in")
					return r_home(id)
			return render_template('login.html', error='Invalid ID or Password')
		return render_template('login.html')

	@app.route('/student/home')
	def student_home():
		student_id = request.cookies.get('student_id')
		if student_id:
			db = getdatabase()
			subjects = len(db.retrieve_table('subject'))
			name =db.retrieve_table('students') 
			qname=[list(i[1:4]) for i in name if i[0]==int(student_id) ][0]
			name=" ".join(qname)
			todays_attendance = db.retrieve_todays_attendance('attendance_log',
					date=str(datetime.datetime.today()).split(' ')[0])
			for i in todays_attendance:
				if int(student_id) == int(i[0]):
					timelog = str(i[1])
					subs = attendance_time_checker(timelog)
					return render_template('student/index.html', subjects=subs, time_logined=timelog, didlogin=True, mysub=subjects,name=name)
			subs = attendance_time_checker("")
			return render_template('student/index.html', subjects=subs, didlogin=False, mysub=subjects,name=name)
		return redirect(url_for('student_login'))

	@app.route('/student/subjects')
	def student_subjects():
	
		student_id = request.cookies.get('student_id')
		if student_id:
			db = getdatabase()
			subjects = db.retrieve_table('subject')
			name =db.retrieve_table('students') 
			qname=[list(i[1:4]) for i in name if i[0]==int(student_id) ][0]
			name=" ".join(qname)
			return render_template('student/subjects.html', subjects=subjects,name=name)
		return redirect(url_for('student_login'))

	@app.route('/student/logout')
	def student_logout():
		resp = redirect(url_for('student_login'))
		resp.set_cookie('student_id', '', expires=0)
		return resp
		
	@app.route("/student/profile")
	def sprofile():
		student_id = request.cookies.get('student_id')
		if student_id:
			db = getdatabase()
			subjects = db.retrieve_table('subject')
			name =db.retrieve_table('students') 
			qname=[list(i[1:4]) for i in name if i[0]==int(student_id) ][0]
			info=[list(i) for i in name if i[0]==int(student_id) ][0]
			name=" ".join(qname)    
			return render_template("student/profile.html",info=info,subjects=subjects)