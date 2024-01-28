#!/usr/bin/python3
"""
script that starts a Flask web application:
Your web application must be listening on 0.0.0.0, port 5000
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text
    variable (replace underscore _ symbols with a space )
    /python/(<text>): display “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
        The default value of text is “is cool”
    /number/<n>: display “n is a number” only if n is an integer
    /number_template/<n>: display a HTML page only if n is an integer:
        H1 tag: “Number: n” inside the tag BODY
You must use the option strict_slashes=False in your route definition
"""
from flask import Flask, render_template, abort
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/(<text>)', strict_slashes=False)
def c(text):
    """
    returns C ” followed by the value of the text variable
    (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route("/python", strict_slashes=False)
@app.route("/python/(<text>)", strict_slashes=False)
def p(text="is cool"):
    """
    returns “Python ”, followed by the value of the
    text variable (replace underscore _ symbols with a space )
    """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """returns “n is a number” only if n is an integer"""
    try:
        int(n)
        return f"{n} is a number"
    except ValueError:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """
    return a HTML page only if n is an integer:
    H1 tag: “Number: n” inside the tag BODY
    """
    try:
        int(n)
        return render_template("5-number.html", n=n)
    except ValueError:
        abort(404)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
