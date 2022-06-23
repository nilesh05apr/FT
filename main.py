import tweepy
import pandas as pd
import os
from dotenv import main
import time
import pickle

def configure():
    main.load_dotenv()
configure()


#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)









CES = [] #critically endangered species
with open('Critically Endangered Species.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        CES.append(t)
f.close()
#print(CES[0])




PES = [] #possibly extinct species
with open('Possibly Extinct.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        PES.append(t)
f.close()
#print(PES[0])




VS = [] #vulnerable species
with open('Vulnerable Species.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        VS.append(t)
f.close()
#print(VS[0])


def get_tweets(query):
    query = query + "-filter:retweets"
    tweets = tweepy.Cursor(api.search,q=query,lang="en").items(10)
    tw_copy = []
    for tweet in tweets:
        tw_copy.append(tweet)
    print(f"{len(tw_copy)} tweets found for {query}")
    return tw_copy

def get_tweet_df(species):
    tweets_df = pd.DataFrame()
    for s in species:
        start = time.process_time()
        tweets_copy = get_tweets(s)
        end = time.process_time()
        print(f"Time for keyword {s}: {end-start}")
        # time.sleep(10)
        if len(tweets_copy) >= 1000:
          SLEEP_TIME = 120
        elif len(tweets_copy) >= 100:
          SLEEP_TIME = 30
        else:
          SLEEP_TIME = 15
        for tweet in tweets_copy:
            hashtags = []
            try:
                for hashtag in tweet.entities["hashtags"]:
                    hashtags.append(hashtag)
                text = api.get_status(id=tweet.id, tweet_mode='extended').full_text
            except:
                pass

            if tweet.coordinates != None:
              coord = tweet.coordinates['coordinates']
            else:
              coord = None

            tweets_df = pd.concat([tweets_df,pd.DataFrame({
                'user_name': tweet.user.name,
                "user_description": tweet.user.description,
                "user_location": tweet.user.location,
                "user_verification": tweet.user.verified,
                "date": tweet.created_at,
                "text": text,
                "hashtags": [hashtags if hashtags else None],
                "source": tweet.source,
                "retweets": tweet.retweet_count
                })],axis=0)

            tweets_df = tweets_df.reset_index(drop=True)
        time.sleep(SLEEP_TIME)
    return tweets_df


# Tweets_C = get_tweet_df(CES)
# Tweets_C.to_csv("Tweets_CE_Species.csv")

# Tweets_V = get_tweet_df(VS)
# Tweets_V.to_csv("Tweets_V_species.csv")

# Tweets_E = get_tweet_df(PES)
# Tweets_E.to_csv("Tweets_PE_species.csv")
    