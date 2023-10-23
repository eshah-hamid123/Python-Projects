# import sqlite3
# db = sqlite3.connect('books-collection.db')
# cursor = db.cursor()
# #cursor.execute('CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)')
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute('INSERT INTO books VALUES(1, "Harry Potter", "J.K.Rowling", "9.3")')
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    review = db.Column(db.Float)


with app.app_context():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    db.create_all()
    new_book = Book(id=2, title='The Choice', author='sparks', review=9.3)
    db.session.add(new_book)
    db.session.commit()


