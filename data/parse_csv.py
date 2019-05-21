import numpy as np 
import pandas as pd 
import os 

datapath = "."
datafiles = os.listdir(datapath)

print(datafiles)
df = pd.read_csv("./jpn_indices.csv", encoding="utf-8")
print(df.head())

# df[0:1000].to_csv("./test.csv", index=False)
print(df.shape)