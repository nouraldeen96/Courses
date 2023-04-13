from flask import render_template
from courses import app
from courses import api


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/admin')
def admin():
    return render_template("Admin.html")

@app.route('/update')
def update():
    return render_template("updatecourse.html")

@app.route('/more_info')
def more_info():
    return render_template("more_info.html")

@app.route('/allusers')
def all_users():
    return render_template("show_all_users.html")

@app.route('/addcourse')
def add_course():
    return render_template("addcourse.html")

@app.route('/allstudents')
def all_students():
    return render_template("showstudents.html")

@app.route('/showteachers')
def show_teachers():
    return render_template("show_all_teachers.html")

@app.route('/settings')
def settings():
    return render_template("settings.html")

@app.route('/my_courses')
def my_courses():
    return render_template("mycourses.html")
