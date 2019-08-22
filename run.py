import os
from flask import Flask, render_template, flash, session, request, redirect, url_for
app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form["username"]
        session['username'] = username
        return redirect(url_for('start_session', user = username))
    return render_template("index.html")

@app.route('/welcome/<user>')
def start_session(user):
    return render_template('welcome.html', user=user)

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=os.environ.get('PORT'),
    debug = True)