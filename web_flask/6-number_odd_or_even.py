#!/usr/bin/python3
'''
Contains a script that starts a flask application
'''
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    '''Returns a string'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Returns a string'''
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''
    Display “C ” followed by the value of the text variable
    replace underscore _ symbols with a space
    '''
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    '''
    Display “Python ”, followed by the value of the text variable
    replace underscore _ symbols with a space
    '''
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''display “n is a number” only if n is an integer'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    '''Return template only if n is an integer'''
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    '''Return template only if n is an integer'''
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
