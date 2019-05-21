import numpy as np 
import pandas as pd 
import os 

datapath = "."
datafiles = os.listdir(datapath)

# print(datafiles)
df = pd.read_csv("./test.csv")

df['a'].tolist()

# print(df)
sentences=[]
for sentence in df['a']:
    sentences.append([sentence[sentence.replace("\t"," ",1).find("\t")+1:]])
# print(sentences)

