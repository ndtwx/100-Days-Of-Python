from flask import Flask
import random

correct_number = random.randint(0, 9)
print(correct_number)

app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 to 9</h1>" \
           '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamE1YTR6YWVjMTBuMGQzY3dxdG1rMXZqaXVwNGNraGh4YXI4czE1YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/26gR1wYpogPiJQuwo/giphy.gif">'


@app.route('/<int:guess>')
def check_number(guess):
    if guess > correct_number:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    elif guess < correct_number:
        return "<h1 style='color: red'>Too low, try again!</h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"


if __name__ == "__main__":
    app.run(debug=True)
