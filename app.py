import pickle
import pandas as pd


f = open("CesTweets.pkl","rb")
data = pickle.load(f)
f.close()

print(data)

