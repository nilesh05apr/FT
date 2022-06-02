import tweepy
import pandas as pd
import os
from dotenv import main
import time
def configure():
    main.load_dotenv()
configure()


#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(os.getenv('API_KEY'), os.getenv('API_KEY_SECRET'))
auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
api = tweepy.API(auth)





def get_tweets_for_keyword(q, max_tweets=1000):
    """This function gets tweets for a particular keyword"""
    created_at_list = []
    id_str_list = []
    text_list = []
    user_id_list = []
    user_name_list = []

    try:
        for tweet in tweepy.Cursor(api.search_tweets,
                                   q=q,
                                   count=100,
                                   result_type="recent",
                                   include_entities=True,
                                   lang="en").items(max_tweets):

            created_at_list.append(tweet.created_at)
            id_str_list.append(tweet.id_str)
            text_list.append(tweet.text)
            user_id_list.append(tweet.user.id_str)
            user_name_list.append(tweet.user.name)


        # Create a Pandas DataFrame from the data.
        df = pd.DataFrame({'created_at': created_at_list,
                                'id': id_str_list, 
                                'text': text_list, 
                                'user_id': user_id_list, 
                                'user_name': user_name_list, 
                                })

        tweets_file_name = "tweets_" + q.replace(" ", "_") + ".csv"
        return df
    except tweepy.errors.TweepyException as err:
        print(err)



new_df = get_tweets_for_keyword('Sumatran rhinoceros',max_tweets=5)
print(new_df)

CES = [] #critically endangered species
with open('Critically Endangered Species.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        CES.append(t)
f.close()
print(CES[0])




PES = [] #possibly extinct species
with open('Possibly Extinct.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        PES.append(t)
f.close()
print(PES[0])




VS = [] #vulnerable species
with open('Vulnerable Species.txt','r') as f:
    l = f.readlines()
    for name in l:
        t = ''.join(i for i in name if not i.isdigit())
        t = t.replace('.','')
        VS.append(t)
f.close()
print(VS[0])


CES_Tweets = {}
for species in CES:
    start = time.process_time()
    tweets = get_tweets_for_keyword(species,100)
    end = time.process_time()
    print(species,(end-start))
    CES_Tweets[species] = tweets


print(CES_Tweets)