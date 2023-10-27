# Name: Nikhil Dhage
# Class: INF601 - Advanced Programming in Python
# Project: Weather Web App in Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, db, requests, os
from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Initialize the Database with the SQL Schema
db.init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = db.get_db('SELECT * FROM users WHERE username = ?', (username,), one=True)

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('weather'))
        flash('Invalid credentials!')
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])

        try:
            db.post_db('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!')
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)

