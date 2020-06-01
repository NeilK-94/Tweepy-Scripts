import tweepy
from datetime import datetime, timedelta
import secrets as s
# Options
test_mode = True # Set to false to arm the program!
verbose = True # Allows for feedback on deletion/unfavoriting of tweets
delete_tweets = True # Set to true to activate delete tweets
unfav_tweets = True # Set to true to activate unfavorite tweets
days_to_keep = 7 # Keep tweets within this number of days to the present time
max_favs = 10 # Don't delete a tweet if it has more than this number of favorites
max_rts = 10 # Don't delete a tweet if it has more than this number of retweets
 
# Authentication and API (Never publicise keys and secrets)
auth = tweepy.OAuthHandler(s.consumer_key, s.consumer_secret)
auth.set_access_token(s.access_token, s.access_token_secret)
# Rather than just exiting the program, if the rate limit is reached, sleep for a time then run again
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True) 

# Set cutoff date, using utc
cutoff_date = datetime.utcnow() - timedelta(days=days_to_keep)
 
# Delete old tweets if option set to true
if delete_tweets:
    # Get all timeline tweets (items)
    print ("Retrieving timeline tweets...")
    timeline = tweepy.Cursor(api.user_timeline).items()
    deletion_count = 0
    ignored_count = 0

    #   For every tweet on the timeline
    for tweet in timeline:
        # Where tweets are older than cutoff date or have under the specified likes and rt's
        if tweet.created_at < cutoff_date and tweet.favorite_count < max_favs and tweet.favorite_count < max_rts:
            if verbose: #   If set, print tweet information as deleted
                print ("Deleting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text.encode("utf-8")))
            if not test_mode:
                api.destroy_status(tweet.id) #   Delete the tweet
            deletion_count += 1
        else:
            ignored_count += 1
 
    print ("Deleted %d tweets, ignored %d" % (deletion_count, ignored_count))
else:
    print ("Not deleting tweets")

# Unfavorite old tweets if option set to true
if unfav_tweets:
    print("Retrieving favorited tweets")
    favorites = tweepy.Cursor(api.favorites).items()
    unfav_count = 0
    kept_count = 0
    #   For tweet in favorites
    for tweet in favorites:
        if tweet.favorite_count > 1:
            if verbose:
                print ("Unfavoriting %d: [%s] %s" % (tweet.id, tweet.created_at, tweet.text.encode("utf-8")))
            if not test_mode:
                api.destroy_favorite(tweet.id)
            unfav_count += 1
        else:
            kept_count += 1
    print("Unfavorited %d tweets, kept %d" % (unfav_count, kept_count))
else:
    print("Not unfavoriting tweets")
        



