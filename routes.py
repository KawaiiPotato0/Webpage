from app import app
from flask import render_template, url_for,

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/register')
def profile():
    return render_template("reister.html")

@app.route('/login')
def profile():
    return render_template("login.html")