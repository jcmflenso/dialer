#Dialer System
#02/15/2016
#0.0.7

from flask import Flask, url_for, request, redirect, render_template, flash, make_response

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form.get('userid'),request.form.get('passwd')):
            flash('Succesfully logged in')
            response = make_response(redirect(url_for('welcome')))
            response.set_cookie('userid', request.form.get('userid'))
            return response
        else:
            error = 'Incorrect username and password'

    return render_template('index.html', error=error)

@app.route('/logout')
def logout():
    response = make_response(redirect(url_for('login')))
    response.set_cookie('userid','',expires=0)
    return response


def valid_login(userid,passwd):
    if not userid:
        return False
    elif userid == passwd:
        return True
    else:
        return False

@app.route('/')
def welcome():
    userid = request.cookies.get('userid')
    if userid:
        return render_template('welcome.html', userid=userid)
    else:
        return redirect(url_for('login'))




if __name__ == "__main__":
    app.debug = True
    app.secret_key = 'flenso'
    app.run()
