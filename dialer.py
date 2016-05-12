#Dialer System
#02/15/2016
#0.0.7

from flask import Flask, url_for, request, redirect, render_template, flash, session
import logging
from logging.handlers import RotatingFileHandler
app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('userid'),request.form.get('passwd')):
            flash('Succesfully logged in')
            session['userid'] = request.form.get('userid')
            return redirect(url_for('welcome'))
        else:
            error = 'Incorrect username and password'
            app.logger.warning('Incorrect username and password for (%s)', request.form.get('userid'))
    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    session.pop('userid',None)
    return redirect(url_for('login'))


def valid_login(userid,passwd):
    if not userid:
        return False
    elif userid == passwd:
        return True
    else:
        return False

@app.route('/')
def welcome():
    userid = session.get('userid')
    if userid:
        return render_template('welcome.html', userid=userid)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.debug = True
    app.secret_key = '\xa2/Y\xf2\x15?q\xf4\xbe"\xb1\x91\x93\x8b\xad\n\xd0K\xed/8\x8d\\i'
    handler = RotatingFileHandler('error.log',maxBytes=10000,backupCount=1)
    handler.setLevel(logging.DEBUG)
    #formatter = logging.Formatter('%(asctime)s')
    #app.logger.addHandler(formatter)
    app.logger.addHandler(handler)
    app.run()
