#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def ooh_filters():
    """this function shows a page of filterable things"""
    states = storage.all(State)
    amenity = storage.all(Amenity)
    return render_template('10-hbnb_filters.html', sorted_states=states,
                           amenity=amenity)


@app.teardown_appcontext
def app_teardown(arg):
    """this function closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0')
