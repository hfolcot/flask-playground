import os
from flask import Flask, render_template, flash
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    flash("Hello")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host="127.0.0.1",
    port="5000",
    debug = True)