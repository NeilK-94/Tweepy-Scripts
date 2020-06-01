# Game plan
# 1. Connect to Twitter API
# 2. Configure options
# 3. Get a list of account I follow (id)
# 4. call a method that processes each account 
# 4.1.     if account meets criteria - unfollow
# 4.2.     else return
# 5. print out the number of unfollowed and kept accounts

import tweepy
import secrets as s

# Connect to Twitter API
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
api = tweepy.API(auth)

# Configure options
test_mode = True

# Get a list of accounts I follow
friends = tweepy.Cursor(api.friends).items()
i = 0
unfollowed_count = 0
for friend in friends:
    i += 1
    print(i, ". Unfollowing: %s, ID: %d" % (friend.screen_name, friend.id))
    if not test_mode:
        api.destroy_friendship(friend.id)
    unfollowed_count += 1

print("Unfollowed: %d accounts" % (unfollowed_count))
