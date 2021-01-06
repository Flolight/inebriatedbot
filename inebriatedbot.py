import tweepy
import os

# Get values from env variables
CONSUMER_KEY= os.getenv('CONSUMER_KEY')
CONSUMER_SECRET= os.getenv('CONSUMER_SECRET')
ACCESS_KEY= os.getenv('ACCESS_KEY')
ACCESS_SECRET= os.getenv('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True,
    wait_on_rate_limit_notify=True)

try:
    api.verify_credentials()
    print("Authentication OK")
    #api.update_status("This my first tweet!")
    print(api.me())
except:
    print("Error during authentication")