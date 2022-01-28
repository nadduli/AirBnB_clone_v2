#!/usr/bin/python3
""" Starts a flask web application """


from flask import Flask
from flask import render_template


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


@app.route('/number/<int:n>', strict_slashes=False)
def number_flask(n):
    """ display number """
    if type(n) == int:
        return '%i is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def template_flask(n):
    """ returns html template with a number """
    if type(n) == int:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_flask(n):
    """ returns html template with a number """
    if type(n) == int:
        return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
