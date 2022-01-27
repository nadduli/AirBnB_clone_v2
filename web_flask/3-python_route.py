#!/usr/bin/python3
""" Starts a flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbtn():
    """ returns a hello string to holberton """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_holberton():
    """ returns holberton """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """ returns string text after replacing underscores with spaces """
    words = "C "
    words += text.replace('_', ' ')
    return words


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_flask(text):
    """ returns text after replacing underscores with spaces,
        default = 'is cool'
    """
    text = text.replace('_', ' ')
    return 'Python %s' % text


if __name__ == '__main__':
    app.run(host='0.0.0.0')
