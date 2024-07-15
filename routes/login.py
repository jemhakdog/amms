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