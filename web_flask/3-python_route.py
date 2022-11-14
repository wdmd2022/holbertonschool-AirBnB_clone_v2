#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask
from markupsafe import escape

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


if __name__ == "__main__":
    app.run('0.0.0.0')
