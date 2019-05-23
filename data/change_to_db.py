import numpy as np 
import pandas as pd 
import os 
from random import choice, shuffle, sample

temp_grammar_list = ['だって','の','は|1','が','のは','のに','だが','中途半端','で','ので','を','のを','から','と','や','とする','もの','こと']

for i, item in enumerate(temp_grammar_list):
    temp_grammar_list[i] = " " + item + " "

datapath = "."
datafiles = os.listdir(datapath)

# print(datafiles)
df = pd.read_csv("./test.csv")

df['a'].tolist()

# print(df)
sentences=[]
for sentence in df['a']:
    sentences.append([sentence[sentence.replace("\t"," ",1).find("\t")+1:]])
rand_sentence = str(choice(sentences))
print(rand_sentence)
print(len(rand_sentence))
shuffle(temp_grammar_list)
for i, item in enumerate(temp_grammar_list):
    if item in rand_sentence:
        print(rand_sentence.replace(item, ' ____ '))

        print(item)
        print(temp_grammar_list[i])
        temp_grammar_list.pop(i)
        print(sample(temp_grammar_list, k=3))
        break
print("Done.")