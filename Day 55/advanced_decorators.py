"""
Advance Decorator with *args and **kwargs
"""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # Rendering HTML Elements
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif" width=200>'


# Advanced Python Decorator Functions
def logging_decorator(route_function):
    def wrapper(*args):
        result = route_function(*args)
        return str(result)  # Return the original result or None if you don't want to modify it

    return wrapper


# Flask route with the logging_decorator
@app.route("/testing_1")
@logging_decorator
def a_function(num1=5, num2=60):
    return num1 * num2


if __name__ == "__main__":
    app.run(debug=True)
