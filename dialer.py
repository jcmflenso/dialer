#Dialer System
#02/15/2016
#0.0.4
from flask import Flask, url_for, request, redirect, render_template, flash

app = Flask(__name__)

@app.route('/')
def index():
    #return "Index Page"
    return redirect(url_for('login'))

@app.route('/')
@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['userid'],request.form['passwd']):
            flash('Succesfully logged in')
            return redirect(url_for('welcome', userid=request.form.get('userid')))
        else:
            error = 'Incorrect username and password'

    return render_template('index.html', error=error)

def valid_login(userid,passwd):
    if userid == passwd:
        return True
    else:
        return False

@app.route('/welcome/<userid>')
def welcome(userid):
    return render_template('welcome.html', userid=userid)




if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'flenso'
    app.run()
