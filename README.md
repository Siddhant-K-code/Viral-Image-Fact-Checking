# Viral-Image-Fact-Checking
An online tool to verify if a viral image shared online recently is actually from recent times or if it has been picked up from a past incident to raise tensions over a controversial viral discussion. We’d effectively be making a tool to detect and flag fake news

HOSTED URL:-
http://coderpd.me/Viral-Image-Fact-Checking/


REQUIREMENTS:- 
pycurl
flask
flask_cors
bs4
operations
pandas
numpy
requests
certifi


server.py - to host http server either locally or remotely on AWS etc.
Usuage: python server.py

run.py - to run the application in terminal
Usage: python run.py

index.html - run the application in browser
javascript.js - perform functions .  (edit the server dns/ip with your ip before running)

operations.py -  currently working to add other operations like getting the oldest corresponding news, image first time appeared on internet

server.py - working fine ...  will add more features like adding Machine Learning algorithms ..@app.route('/history') @app.route('/data') has been left blank for the reason .  
