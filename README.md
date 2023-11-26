## miniproject3ND
INF601 - Advanced Programming in Python  
Nikhil Dhage



### Description
This project uses Flask to deploy a small weather web app. It integrates with the OpenWeatherMap API to fetch real-time weather data. Users can register, login, and view weather details for different cities.

### Frameworks/API 
This project uses the following packages and API
```
Pythoon :3.11.5
Flask : 3.0.0
Bootstrap :5.3.2
OpenWeatherMAPAPI: 
```

### Pip Install Requirements
Please run the following

```
pip install -r requirements.txt
```

### How to Run
To start the Flask development server, please type the following commands:

For **Windows**:

```
flask --app app run
```

### How to Quit
Use this command to quit the flask app or terminate the app 
in the console of your editor'
```
Ctrl + C 
```

### How to generate API_KEY
1. Got to the url below
```
https://openweathermap.org
```

2. Then navigate to create a free account or register
and register with a free plan

3. Then once you have created a free account
sign in 

4. Navigate to my api keys drop down option below your account name
 
5. Generate a new API Key 

### Integrating the API_KEY
1. Create a .eenv under the venv folder of your virtual environment
    Please make sure you are using virtual environment and 
    interpreter.

2.  Create a new variable called SECRET_KEY and set it to 
    some text 
     ```
    Ex. SECRET_KEY='MY_SECRET_KEY'
    ``` 
   3. Then create a another variable called API_KEY 
   This is KEY that will be referred to by the app for 
   any requests sent to the API
4.  Find the API_KEY you generated on the open weather api website 
5. Set theAPI_KEY vaariable to the generated API_KEY from open weather api
    ```
   Ex. API_KEY='abcd1234'
   ```
