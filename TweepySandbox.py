import tweepy
from datetime import datetime, timedelta
import secrets as s

# authentication and api (Never publicise keys and secrets)
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
# Rather than just exiting the program, add last 2 parameters to sleep if rate limit reached
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# #  get all tweets on the authenticated user's timeline
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#    print(tweet.text)


# # Get the User's object/model for twitter...
# user = api.get_user('@kickarseHD')

# print("Screen name: ", user.screen_name)
# print("Follower count: ", user.followers_count)
# print("\nFriend names: ")
# for friend in user.friends():
#    print(friend.screen_name)

#  Print  my follower count
me = api.get_user(s.my_username)
i = 0
# Iterate through all of the authenticated user's friends
for follower in tweepy.Cursor(api.followers).items():
    # Process the friend here
    i+= 1
    print(i, follower.screen_name, "==> ", follower.id)
