from flask import Flask

app = Flask(__name__)

# Create a decorator function
def make_bold(function):
    def wrapper_function():
        return f'<b>{function()}</b>'
    return wrapper_function

def make_emphasis(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper
def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

@app.route("/")
def hello_word():
    return "<p> Hello World!</p>"
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "Bye!"


if __name__ == "__main__":
    app.run(debug=True)
