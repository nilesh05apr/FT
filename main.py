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

        data = {'created_at': created_at_list,
                'id': id_str_list, 
                'text': text_list, 
                'user_id': user_id_list, 
                'user_name': user_name_list,}
        # Create a Pandas DataFrame from the data.
        df = pd.DataFrame({'created_at': created_at_list,
                                'id': id_str_list, 
                                'text': text_list, 
                                'user_id': user_id_list, 
                                'user_name': user_name_list, 
                                })

        tweets_file_name = "tweets_" + q.replace(" ", "_") + ".csv"
        return data
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


def get_ces_tweets(CES_Tweets):
    for species in CES:
        start = time.process_time()
        tweets = get_tweets_for_keyword(species,1000)
        end = time.process_time()
        print("Time taken by:{} is {}s".format(species,(end-start)))
        CES_Tweets[species] = tweets
        time.sleep(10)
    return CES_Tweets

def get_vs_tweets(VS_Tweets):
    for species in VS:
        start = time.process_time()
        tweets = get_tweets_for_keyword(species,1000)
        end = time.process_time()
        print("Time taken by:{} is {}s".format(species,(end-start)))
        VS_Tweets[species] = tweets
        time.sleep(10)
    return VS_Tweets

def get_pes_tweets(PES_Tweets):
    for species in PES:
        start = time.process_time()
        tweets = get_tweets_for_keyword(species,1000)
        end = time.process_time()
        print("Time taken by:{} is {}s".format(species,(end-start)))
        PES_Tweets[species] = tweets
        time.sleep(10)
    return PES_Tweets


def main():
    CES_Tweets = {}
    ces_tweets_ = get_ces_tweets(CES_Tweets)
    VS_Tweets = {}
    vs_tweets_ = get_vs_tweets(VS_Tweets)
    PES_Tweets = {}
    pes_tweets_ = get_pes_tweets(PES_Tweets)


#print(CES_Tweets)

if __name__ == '__main__':
    CES_Tweets = {}
    ces_tweets = get_ces_tweets(CES_Tweets)
    with open('CesTweets.pkl','wb') as f:
        pickle.dump(ces_tweets,f)

    VS_Tweets = {}
    vs_tweets_ = get_vs_tweets(VS_Tweets)
    with open('VsTweets.pkl','wb') as f:
        pickle.dump(vs_tweets_,f)

    PES_Tweets = {}
    pes_tweets_ = get_pes_tweets(PES_Tweets)
    with open('PesTweets.pkl','wb') as f:
        pickle.dump(pes_tweets_,f)

    