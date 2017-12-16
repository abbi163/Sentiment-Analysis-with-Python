# for twitter API, pip install tweepy
# for redis database connection, pip install redis
# for sentiment analysis , pip install textblob
import tweepy
import redis
from textblob import TextBlob

r = redis.Redis('localhost')

# sign in to app.twitter.com and make tokens and consumer key
consumer_key = 'your-consumer-key'
consumer_secret = 'your-consumer-secret'

access_token = 'your-access-token'
access_token_secret = 'your-access-token-secret'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)
public_tweets = api.search(q="Ripple",count =10000000)
for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	data = {"Tweet":tweet.text, "Analysis":analysis.sentiment}
	r.sadd('DataSet', data)