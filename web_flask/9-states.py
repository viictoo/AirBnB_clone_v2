#!/usr/bin/python3
"""show states

Returns:
    html: render template
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """display states from storage"""
    states = storage.all(State)
    return render_template("9-states.html", states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id=None):
    """display states from storage"""
    states = storage.all(State).values()
    if id is None:
        return render_template("9-states.html", state=state)
    state = None
    for ids in states:
        if ids.id == id:
            state = ids
    return render_template("9-states.html", state=state)


@app.teardown_appcontext
def teardown(self):
    """close session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
