import tweepy
from key import br_token, api_key, api_sec_key, ac_key, ac_sec_key

api = tweepy.Client(bearer_token = br_token, consumer_key = api_key, consumer_secret = api_sec_key, access_token = ac_key, access_token_secret = ac_sec_key)
f = open("list.txt", "r")
persons = []

for line in f:
    url = line.rstrip()
    url_id = url.replace("https://twitter.com/", "")
    user_value = api.get_user(username=url_id)
    user_id = str(user_value.data["id"])
    persons.append(user_id)