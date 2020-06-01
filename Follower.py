# About
# A script to follow people based on certain parameters:
#     ...Their name, string in their tweet, accounts that follow me (friends), how old the tweet is, how many likes etc
# Could consider first doing a search under those certain paramaters then saving the account details 
#   of those accounts in a csv file locally. Then read in the id's and follow!

# Game plan
# 1. Connect to twitter API
# 2. Configure options
# 3. Search for tweets based on search query 
# 4. If tweet has over a predefined retweet count, follow user
# 5. Print total number of new account followed

# use API.create_friendship to follow an account
# API.search_users(q) to search by user
# API.search(q) t search tweets

import tweepy
import secrets as s
import random

# Connect to Twitter API
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Configure options
test_mode = False
verbose = True # Allows for feedback on deletion/unfavoriting of tweets

#search_query = ["#FollowBack", "#FollowTrain", "#IFollowBack", "#Followers"]
search_query = "#FollowBack"

# # 3. Search for accounts based on random selection from search query (result_type options = mixed, popular, recent)
tweets = tweepy.Cursor(api.search, q = search_query, lang = 'en', result_type='popular').items(5)

ignored_count = 0
followed_count = 0
i = 0

print("Searching for: %s" % (search_query))

for tweet in tweets:
    i += 1
    print(i, "Account: %s, Favorite count: %d " % (tweet.user.screen_name, tweet.retweet_count))
    
    if tweet.favorite_count > 100:
        if verbose: 
            print("Following: %s\n" % (tweet.user.screen_name))
            followed_count += 1
        if not test_mode:
            api.create_friendship(tweet.user.id)
    else:
        ignored_count += 1

print("\nFollowed %s new accounts \nIgnored %s accounts" % (followed_count, ignored_count))
