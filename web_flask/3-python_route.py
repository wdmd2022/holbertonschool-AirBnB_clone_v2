#!/usr/bin/python3
"""
Script that start a Flask application listening on 0.0.0.0:5000
Route '/' displays 'Hello HBNB!'
Route '/hbnb' displays 'HBNB'
Route '/c/<text>' displays 'C <text>'
    (replace '_' with ' ')
Route '/python/<text>' displays 'Python <text>'
    (replace '_' with ' ')
    (default value = 'is cool')
"""


from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    """ prints Hello HBNB! """
    return ("Hello HBNB!")


@app.route('/hbnb')
def hbnb():
    """ prints HBNB """
    return("HBNB")


@app.route('/c/<text>')
def c(text):
    """ prints 'C <text>' """
    val = "C {}".format(text).replace("_", " ")
    return(val)


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """ prints 'Python <text>' """
    return("Python {}".format(text).replace("_", " "))


if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
