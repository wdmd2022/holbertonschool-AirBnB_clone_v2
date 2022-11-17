#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from flask import render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """this function returns some hello text"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def just_hbnb():
    """this function returns some hello text"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """this function returns some text based on the URL"""
    text_string = escape(text)
    text_string_to_return = ' '.join(text_string.split('_'))
    return "C {}".format(text_string_to_return)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """this function returns some text based on a different URL"""
    text_string = escape(text)
    text_string_to_return = ' '.join(text_string.split('_'))
    return "Python {}".format(text_string_to_return)


@app.route("/number/<int:n>", strict_slashes=False)
def number_display(n):
    """this function returns some text about a number in the URL"""
    return "{:d} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """this function returns a rendered HTML page based on a number"""
    return render_template('5-number.html', numbywumby=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """this function returns a rendered HTML page based on a number"""
    return render_template('6-number_odd_or_even.html', mysterynumber=n)


@app.route("/states_list", strict_slashes=False)
def list_the_states():
    """this function returns a rendered HTML page of states"""
    states = storage.all(State)
    return render_template('7-states_list.html', the_states=states)


@app.teardown_appcontext
def app_teardown(arg):
    """this function closes the storage"""
    storage.close()


if __name__ == "__main__":
    app.run('0.0.0.0')
