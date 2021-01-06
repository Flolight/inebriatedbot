import tweepy
import os
import requests
import json

# Get values from env variables
CONSUMER_KEY= os.getenv('CONSUMER_KEY')
CONSUMER_SECRET= os.getenv('CONSUMER_SECRET')
ACCESS_KEY= os.getenv('ACCESS_KEY')
ACCESS_SECRET= os.getenv('ACCESS_SECRET')

def twitterAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getJoke(category="Any", blacklistFlags="religious,racist,sexist"):
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags={blacklistFlags}"
    #print(url)
    return requests.get(url)

api = twitterAuth() 

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


obj = getJoke(category="Any").json()
tweet = f"Hey! Let's have a joke...\n[{obj['category']}]\n"

print()
if obj['type'] != 'twopart':
    tweet += obj['joke']
else:
    tweet += f"- {obj['setup']}"
    tweet += f"\n- {obj['delivery']}"

print(tweet)
api.update_status(tweet)