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
    """ Authenticate user using Twitter API generated credentials """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    return tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

def getJoke(category="Any", blacklistFlags="religious,racist,sexist"):
    """
    Get a joke from https://v2.jokeapi.dev API
    """
    url = f"https://v2.jokeapi.dev/joke/{category}?blacklistFlags={blacklistFlags}"
    return requests.get(url)

def followAllMyFollowers(twitterApi):
    """ Follow all the followers of @inebriatedbot """
    for follower in tweepy.Cursor(twitterApi.followers).items():
        # print(follower.name)
        follower.follow()

def bot_joke_mode(twitterApi):
    print("//// bot_joke_mode ////")

    apiResponseJson = getJoke(category="Any").json()
    tweet = f"Hey! Let's have a joke...\n[{apiResponseJson['category']}]\n"

    if apiResponseJson['type'] != 'twopart':
        tweet += apiResponseJson['joke']
    else:
        tweet += f"- {apiResponseJson['setup']}"
        tweet += f"\n- {apiResponseJson['delivery']}"

    print(tweet)
    twitterApi.update_status(tweet)

def bot_follow_followers_mode(twitterApi):
    print("//// bot_follow_followers_mode ////")
    followAllMyFollowers(twitterApi)

def main():
    twitterApi = twitterAuth() 
    try:
        twitterApi.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")

    bot_joke_mode(twitterApi)
    bot_follow_followers_mode(twitterApi)