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
Route '/number/<n>'
    Displays '<n> is a number' if <n> is integer
Route '/number_template/<n>'
    Displays HTML page only if <n> is an integer
    H1 tag: 'Number: <n>'
Route '/number_odd_or_even/<n>'
    Displays HTML page only if <n> is an integer
    H1 tag: 'Number: <n> is even|odd'
"""


from flask import Flask, render_template
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


@app.route('/number/<int:n>')
def number(n=""):
    """ checks type of n, then returns appropriate response """
    return("{} is a number".format(n))


@app.route('/number_template/<int:n>')
def number_template(n):
    """ display html page if n is a number """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ display html page if n is a number """
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
        app.run(host="0.0.0.0", port="5000")
