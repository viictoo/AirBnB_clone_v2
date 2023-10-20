#!/usr/bin/python3
"""script that starts a flask application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """returns passed variable
    """
    text = text.replace('_', ' ')
    return (f'C {text}')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """returns string passed variable
    """
    text = text.replace('_', ' ')
    return (f'Python {text}')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """returns number passed variable
    """
    return (f'{n} is a number')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
