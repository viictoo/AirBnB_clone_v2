#!/usr/bin/python3
"""show states
Returns:
    html: render tamplate
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def statesList():
    """display states from storage"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown():
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
