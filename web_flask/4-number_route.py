#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """A function that is called when the / page is accessed"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that is called when the /hbnb page is accessed"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """A function that is called when the /c/<text> page is accessed"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """A function that is called when the /python/<text> page is accessed"""
    if text:
        return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
