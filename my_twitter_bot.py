
import tweepy
import time 




print("my first twitter bot  ",flush=True)

CONSUMER_KEY = 'LFCPG4sSzCWkzmbjfdIq0d46R'
CONSUMER_SECRET = 'phrkDf3EGqvn0DAYORY9cKXQUypO1hgPZlAPZUaQ3tqx5hSGX8'
ACCESS_KEY = '851490108708540416-fnbYjK4rtzpdHZrl5aXYBiJo9eebndO'
ACCESS_SECRET='YML0CQJwdMT7Lhy5VIPoOZK28VkxAtOLlSr1TJeMVIUt6'



auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

mentions = api.mentions_timeline()

FILE_NAME = 'last_seen_id.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

# for mention in mentions :
#     print(str(mention.id) + '-'+  mention.text) 
#     if '#helloworld' in mention.text.lower():
#         print('found #helloworld!!')
#         print('responding back ...')

def reply_to_tweets():
    print('retrieving and replying to tweets...', flush=True)
    # DEV NOTE: use 1060651988453654528 for testing.
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text, flush=True)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.full_text.lower():
            print('found #helloworld!', flush=True)
            print('responding back...', flush=True)
            api.update_status('@' + mention.user.screen_name +
                    '#HelloWorld back to you!', mention.id)

while True:
    reply_to_tweets()
    time.sleep(15)