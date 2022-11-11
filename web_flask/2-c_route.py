#!/usr/bin/python3
"""
Script that start a Flask application listening on 0.0.0.0:5000
Route '/' displays 'Hello HBNB!'
Route '/hbnb' displays 'HBNB'
Route '/c/<text>' displays 'C <text>' (replace '_' with ' ')
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
    """ prints 'c <text>' """
    val = "C {}".format(text).replace("_", " ")
    return(val)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
