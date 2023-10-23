from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def start_game():
    return '<h1> Guess a number between 0 and 9</h1>' \
            '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=300>'


no = random.randint(0,9)
print(f"No is {no}")

@app.route('/<int:number>')
def guess_number(number):
    if no > number:
        return '<h1>Too low, try again</h1>' \
               '<img src="https://media.giphy.com/media/TgmiJ4AZ3HSiIqpOj6/giphy.gif" width=300>'
    if no < number:
        return '<h1>Too high, try again</h1>' \
               '<img src="https://media.giphy.com/media/MXi8nBJjIBgKbyA1MM/giphy.gif" width=300>'
    else:
        return '<h1>Congratulations you got it</h1>' \
               '<img src="https://media.giphy.com/media/Vq9ortuhLZy3obaEFy/giphy.gif" width=300>'



if __name__ == "__main__":
    app.run(debug=True)
