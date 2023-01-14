#!/usr/bin/python3
""" A script that starts a Flask web application
It must be listening on port 500, 0.0.0.0
It has one route, '/' that displayes 'Hello HBNB'
"""
from flask import Flask

app =  Flask(__name__)

@app.route('/', strict_slashes=False)
def hello();
    """'Hello HBNB'"""
    return "Hello HBNB!"

if __name__ = "__main__":
    app.run(host="0.0.0.0")
