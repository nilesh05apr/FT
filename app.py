import pickle
import pandas as pd
from main import get_tweet_df



VS = [] #vulnerable species
with open('Vulnerable Species.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        VS.append(t)
f.close()
print(VS[0])


Tweets_V = get_tweet_df(VS[:100])
Tweets_V.to_csv("Tweets_V_species_100.csv")
print("Saved till 100")


Tweets_V = get_tweet_df(VS[100:200])
Tweets_V.to_csv("Tweets_V_species_200.csv")
print("Saved till 200")

Tweets_V = get_tweet_df(VS[200:300])
Tweets_V.to_csv("Tweets_V_species_300.csv")
print("Saved till 300")

Tweets_V = get_tweet_df(VS[300:400])
Tweets_V.to_csv("Tweets_V_species_400.csv")
print("Save till 400")


Tweets_V = get_tweet_df(VS[400:500])
Tweets_V.to_csv("Tweets_V_species_500.csv")
print("Saved till 500")

Tweets_V = get_tweet_df(VS[500:])
Tweets_V.to_csv("Tweets_V_species_595.csv")
print("Saved till 595")

