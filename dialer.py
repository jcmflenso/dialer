#Dialer System
#02/15/2016
#0.0.2
from flask import Flask, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    #return "Index Page"
    return redirect(url_for('login'))

@app.route('/')
@app.route('/login')
def login():
    return "Welcome to Marketing Leaders"


if __name__ == "__main__":
    app.debug = True
    app.run()
