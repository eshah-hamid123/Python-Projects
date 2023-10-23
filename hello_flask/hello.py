from flask import Flask

# here __name__ is __main__
#it means code is running in this script or in other words __main__ refers to the current file
app = Flask(__name__)

# app route is the python decorator. When user enters / after url it will take it to the home page
@app.route('/')
def first_program():
    return '<h1 style="text-align: center">Welcome to web dev with Flask.</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://media.giphy.com/media/mh0G4oA8uJ9SiRcVWn/giphy.gif" width=400>'

def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_italic(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_u(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper

# first_program()

@app.route('/bye')
@make_bold
@make_italic
@make_u
def say_bye():
    return 'Bye'

@app.route('/<name>/<int:number>')
def greet(name, number):
    return f'Hello there {name}! You are {number} years old'


if __name__ == "__main__":
    app.run(debug=True)


#$env:FLASK_APP = "hello.py"
# python -m flask run
