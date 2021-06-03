__winc_id__ = 'cc1b724762854e85a8defa04287f708b'
__human_name__ = 'requests'

from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/greet/')
def greet():
    return f"<h1>Hello, World!</h1>"

@app.route('/greet/<name>')
def user(name):
    return render_template('greet.html', name=name)
if __name__ == "__main__":
    app.run(debug=True)