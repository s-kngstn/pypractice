import random
from flask import Flask
app = Flask(__name__)

def header_one(function):
    def wrapper(*args, **kwargs):
        return f"<h1>{function()}</h1>"
    # Renaming the function name:
    wrapper.__name__ = function.__name__
    return wrapper

random_number = random.randint(0, 9)
number = random_number
print(number)

@app.route('/')
@header_one
def home_page():
    return "Guess a number between 0 and 9 <br>" \
           "<img width='400px' src='https://media.giphy.com/media/FuSJ5C7SSHlZCxjC6q/giphy.gif'>"


@app.route('/<int:guess_num>')
def guess(guess_num):
    if guess_num == number:
        return "<h1 style='color: green'>You found me!</h1> <br>" \
               "<img width='400px' src='https://media.giphy.com/media/3o7abldj0b3rxrZUxW/giphy.gif'>"
    elif guess_num > number and guess_num < 10:
        return "<h1 style='color: purple'>Too high, try again!</h1> <br>" \
               "<img width='400px' src='https://media.giphy.com/media/3orieYSIw6FQMsmFQQ/giphy.gif'>"
    elif guess_num < number and guess_num < 10:
        return "<h1 style='color: red'>Too low, try again!</h1> <br>" \
               "<img width='400px' src='https://media.giphy.com/media/7OWLeHt8AGhVl8ADoe/giphy.gif'>"
    else:
        return "<h1>out of range</h1> <br>" \
               "<img width='400px' src='https://media.giphy.com/media/VwoJkTfZAUBSU/giphy.gif'>"

if __name__ == "__main__":
    app.run(debug=True)
