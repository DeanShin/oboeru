from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from database_setup import Base, Sentence, Grammar
from random import shuffle, choice, sample, randint

import numpy as np 
import pandas as pd 
import os 

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

    temp_grammar_list = ['だって','の','は|1','が','のは','のに','だが','で','ので','を','のを','から','と','や','とする','もの','こと']
    for i, item in enumerate(temp_grammar_list):
        temp_grammar_list[i] = " " + item + " "
    datapath = "."
    datafiles = os.listdir(datapath)
    df = pd.read_csv("./test.csv")
    df['a'].tolist()
    sentences=[]
    for sentence in df['a']:
        sentences.append([sentence[sentence.replace("\t"," ",1).find("\t")+1:]])

    sentence_found = False
    for sentence in sentences:
        rand_sentence = choice(sentences)[0]
        print(rand_sentence)
        # print(len(rand_sentence))
        shuffle(temp_grammar_list)
        for i, item in enumerate(temp_grammar_list):
            if item in rand_sentence:
                rand_sentence = rand_sentence.replace(item, ' ____ ')
                sentence_found = True
                print(item)
                correct = temp_grammar_list[i]
                temp_grammar_list.pop(i)
                answers = sample(temp_grammar_list, k=3)
                print(i)
                break
        if sentence_found:
            break
        
        
    correct_pos = randint(0,3)
    answers.insert(correct_pos, correct)


    # sentences = db.session.query(Sentence).all()
    # print(sentences)
    # shuffle(sentences)
    # s = choice(sentences)
    return render_template('learn.html', sentence=rand_sentence, answers=answers, correct_pos=correct_pos)

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
