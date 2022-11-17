#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def city_by_state():
    """this function returns cities, by state"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', sorted_states=states)


@app.teardown_appcontext
def app_teardown(arg):
    """this function closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0')
