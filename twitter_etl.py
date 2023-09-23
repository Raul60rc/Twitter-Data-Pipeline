import tweepy 
import pandas as pd 
import json 
from datetime import datetime 
import s3fs 

access_key = "" 
access_secret = ""
consumer_key = ""
consumer_secret = ""

#Twitter authentication 
auth = tweepy.OAuth1UserHandler(access_key,access_secret)
auth.set_access_token(consumer_key,consumer_secret)


#Creating and API object 
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name = '@elonmusk',
                           count=200,
                           include_rts =False,
                           tweet_mode = 'Extended'
                           )

tweet_list = []
for tweets in tweets:
    text = tweet._json["full text"]

    refined_tweet = {"user": tweet.user.screen_name,
                      "text" : text,
                      "favorite_count": tweet.favorite_count,
                      "retweet_count" : tweet.retweet_count,
                      "created_at" : tweet.created_at}
    
    tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)




