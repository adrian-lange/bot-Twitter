import tweepy
from key import api_key, api_sec_key, ac_key, ac_sec_key

auth = tweepy.OAuthHandler(api_key, api_sec_key)
auth.set_access_token(ac_key, ac_sec_key)
api = tweepy.API(auth)

f = open("list.txt", "r")
persons = []

for line in f:
    url = line.rstrip()
    url_id = url.replace("https://twitter.com/", "@")
    user_value = api.get_user(screen_name=url_id)
    user_id = user_value.id_str
    persons.append(user_id)