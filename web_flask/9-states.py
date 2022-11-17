#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def ll_cool_states(id=None):
    """this function shows a page of states"""
    states = storage.all(State)
    return render_template('9-states.html', sorted_states=states, id=id)

@app.teardown_appcontext
def app_teardown(arg):
    """this function closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0')
