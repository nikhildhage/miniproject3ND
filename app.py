# Name: Nikhil Dhage
# Class: INF601 - Advanced Programming in Python
# Project: Weather Web App in Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3, db, requests, os
from geopy.geocoders import Nominatim
from dotenv import load_dotenv


def configure():
    load_dotenv()


configure()

# Initialize the geolocator
geolocator = Nominatim(user_agent="weather_app")

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# OpenWeatherMap API Configurations
API_URL = f"http://api.openweathermap.org/data/2.5/forecast/daily?zip=zip_code,us&appid=os.getenv('API_KEY')"

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


#TODO: Weather details(City Name, Current Temperature, Weather Condition, Day & Night Temperature), Figure out how to get current day and increment for weather cards
#TODO: Implement api request with zip code


@app.route('/weather', methods=['GET', 'POST'])
def weather():
    weather_data = None
    error = None

    if request.method == 'POST':
        zip_code = request.form.get('zip_code')
        cnt = 6  # for current day + next 5 days
        response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast/daily?zip=" + zip_code + ",us&cnt=" + str(cnt) + "&appid=os.getenv('API_KEY')")
        print(response)

        if response.status_code == 200:
            weather_data = response.json()
            # Check if the response contains an error message
            if 'message' in weather_data and weather_data['cod'] != '200':
                error = weather_data['message']
        else:
            error = "Error fetching the weather data. Please try again later."

    return render_template('weather.html', weather_data=weather_data, error=error)


@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    saved_locations = db.get_db("SELECT * FROM saved_locations WHERE user_id=?", (session['user_id'],))
    return render_template('profile.html', saved_locations=saved_locations)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You are now logged out', 'Info')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

