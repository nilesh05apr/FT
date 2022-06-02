import pickle
import pandas as pd


f = open("CES_data.pkl","r")
data = f.read()
f.close()

print(data)