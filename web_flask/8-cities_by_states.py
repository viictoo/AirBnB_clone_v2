#!/usr/bin/python3
"""show states

Returns:
    html: render template
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """display states from storage"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exception):
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
