# About
# A script to retweet tweets  usng a certain query based on certain parameters:

# Game plan
# 1. Connect to twitter API
# 2. Configure options
# 3. Search for tweets based on search query 
# 4. If tweet has over a predefined retweet count, retweet it
# 5. Print total number of tweets retweeted

import tweepy
import secrets as s
import random

# Connect to Twitter API
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Configure options
test_mode = True # Set to false to arm the program!
verbose = True # Allows for feedback on deletion/unfavoriting of tweets

# search_query = ["#FollowBack", "#FollowTrain", "#IFollowBack", "#Followers"]
search_query = "#Trump"
# # 3. Search for accounts based on random selection from search query 
tweets = tweepy.Cursor(api.search, q = search_query, lang = 'en').items(5)

ignored_count = 0
retweeted_count = 0
i = 0
print("Searching for: %s" % (search_query))
# If tweet has a certain number of retweets, retweet it(retweet_count=0, favorite_count=0)
for tweet in tweets:
    i += 1
    print(i, "Retweet count: %d" % (tweet.retweet_count))

    if tweet.retweet_count > 100:
        if verbose: #   If set, print tweet information as deleted
                print ("Retweeting %s: [%s] %s" % (tweet.user.screen_name, tweet.created_at, tweet.text.encode("utf-8")))
        if not test_mode:
            api.retweet(tweet.id)
        retweeted_count += 1
    else:
        ignored_count += 1


print("Retweeted %d tweets, ignored %d" % (retweeted_count, ignored_count))