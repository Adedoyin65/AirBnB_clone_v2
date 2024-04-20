#!/usr/bin/python3
"""A script that starts a Flask web application"""


from flask import Flask, render_template


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
    """A function that is called when the
    /number/<int:n> page is accessed
    """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """A function that is called
    when the /number_template/<int:n> page is accessed
    """
    if isinstance(n, int):
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """A function that is called when the
    /number_odd_or_even/<int:n> page is accessed
    """
    a ='odd' if n % 2 != 0 else 'even'
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', number=n, odd=a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
