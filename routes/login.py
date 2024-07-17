from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(database='amms.db')

def Login(app):
	@app.route("/login")
	def login():
		return render_template("login.html")
from flask import *
import datetime,webbrowser

from manage_database import MySQLDatabase
def getdatabase():
 return  MySQLDatabase(database='amms.db')

def Login(app):
	@app.route("/login")
	def login():
		return render_template("login.html")

	@app.route("/login/faculty")
	def faculty_login():
		return render_template("faculty/index.html")

	@app.route("/login/admin")
	def admin_login():
		return render_template("admin/index.html")
		
	@app.route("/login/process",methods=["POST"])
	def login_process():
		if request.method == 'POST':
			id = request.form.get('id')
			password = request.form.get('password')
			if id.lower() =="admin" and password.lower()=="admin":
				return admin_login()
			else:
				db = getdatabase()
				students = db.retrieve_table('students')
				for student in students:
					if int(id) == int(student[0]):
						resp = redirect(url_for('student_home'))
						resp.set_cookie('student_id', id)
						return resp
				return render_template('login.html', error='Invalid ID or Password')
		return render_template('login.html')
	
	@app.route("/login/faculty")
	def faculty_login():
		return render_template("faculty/index.html")

	@app.route("/login/admin")
	def admin_login():
		return render_template("admin/index.html")