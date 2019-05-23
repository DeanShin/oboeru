from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from database_setup import Base, Sentence, Grammar
from random import shuffle, choice

# Create flask app.
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sentences.sqlite3'
# app.config['SQLALCHEMY_BINDS'] = 'sqlite:///grammar.sqlite3'
db = SQLAlchemy(app)

# Define app routes.
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/learn/")
def learn():
    sentences = db.session.query(Sentence).all()
    print(sentences)
    # shuffle(sentences)
    s = choice(sentences)
    return render_template('learn.html', sentence=s)

@app.route("/practice/")
def practice():
    return render_template('practice.html')

@app.route("/settings/")
def settings():
    return render_template('settings.html')

@app.route("/about/")
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
