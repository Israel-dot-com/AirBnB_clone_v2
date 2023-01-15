#!/usr/bin/python3
"""Starts a Flask web application

The app must be listening on port 500, 0.0.0.0
Routes: 
    /: that displays 'Hello HBNB!'
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Function to display 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
