# simple python script to retrieve a Twitter user's followers
# and save some useful metadata for each in CSV format
#
# this is intended as a simple example, and various optimizations
# for efficiency and robustness are possible

import pandas as pd
import tweepy
import time

def encode (s):
    return s.replace ("\\", "\\\\").replace ("\n", "\\n"
            ).replace ("\r", "\\r").replace ("\t", "\\t")

def get_followers (handle):
    ids = []
    for page in tweepy.Cursor (api.get_follower_ids,       
            screen_name=handle).pages ():
        ids.extend (page)
        time.sleep (61)
        print ("ids: " + str (len (ids)))
    start = 0
    count = len (ids)
    rows = []
    while start < count:
        end = min (start + 100, count)
        for user in api.lookup_users (user_id=ids[start:end]):
            rows.append ({
                "id"                  : user.id_str,
                "handle"              : user.screen_name,
                "displayName"         : encode (user.name),
                "bio"                 : encode (user.description),
                "protected"           : user.protected,
                "followers"           : user.followers_count,
                "following"           : user.friends_count,
                "tweets"              : user.statuses_count,
                "likes"               : user.favourites_count,
                "createTime"          : str (user.created_at)[:19],
                "verified"            : user.verified,
                "defaultProfileImage" : user.default_profile_image,
                "profileImageURL"     : user.profile_image_url_https})
        start = end
        time.sleep (3)
        print ("accounts: " + str (len (rows)))
    df = pd.DataFrame (rows)
    return df

consumer_key = "Your Consumer Key"
consumer_secret = "Your Secret Consumer Key"
auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
api = tweepy.API (auth)

handle = "hogehoge"
df = get_followers (handle)
df.to_csv (handle + "_followers.csv", index=False, encoding="utf-8")