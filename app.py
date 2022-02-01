from turtle import done
import tweepy
import search
from key import api_key, api_sec_key, ac_key, ac_sec_key, br_token


class id_printer(tweepy.Stream):

    def on_status(self, status):

        try:
            if status.user.id_str in tw_ids:
                message = status.text
                status_quote = status.is_quote_status

                # Retweet - person from list

                if message.startswith("RT "):
                    author = status.user.name
                    author_screen_name = f"@{status.user.screen_name}"
                    id_auth = status.id
                    print(id_auth)

                    message_get = api.get_tweet(id=id_auth)
                    message_full = message_get.data["text"]

                    message = message.replace("@", "")
                    message = message.replace("RT ", "")

                    message_full = message_full.replace("@", "")
                    message_full = message_full.replace("RT ", "")
                    dict_post = status.entities
                    first_author_dict_value = dict_post["user_mentions"]
                    first_author_list_value = first_author_dict_value[0]
                    first_author_name = f"{first_author_list_value['name']}"
                    try:
                        try:
                            api.create_tweet(
                                text=f"❗️{author} - retweeted {first_author_name} tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                        except:
                            api.create_tweet(
                                text=f"❗️{author} - retweeted {first_author_name} tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                    except:
                        try:
                            api.create_tweet(
                                text=f"❗️{author} - retweeted {first_author_name} tweet.\n", quote_tweet_id=id_auth)
                        except ValueError:
                            print("Could not create tweet.")

                # Tweet - person from list

                elif status_quote == False:
                    if status.in_reply_to_status_id == None:
                        author = status.user.name
                        author_screen_name = f"@{status.user.screen_name}"
                        id_auth = status.id

                        message = message.replace("@", "")

                        message_get = api.get_tweet(id=id_auth)
                        message_full = message_get.data["text"]
                        message_full = message_full.replace("@", "")
                        try:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - added tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                            except:
                                api.create_tweet(
                                    text=f"❗️{author} - added tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                        except:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - added tweet.\n", quote_tweet_id=id_auth)
                            except ValueError:
                                print("Could not create tweet.")

                    # Comment - person from list

                    else:
                        author = status.user.name
                        author_screen_name = f"@{status.user.screen_name}"

                        id_auth = status.in_reply_to_status_id
                        id_auth2 = status.id

                        message_get = api.get_tweet(id=id_auth2)
                        message_full = message_get.data["text"]

                        for i in message.split():
                            if i.startswith("@"):
                                message = message.replace(i, "")
                        message = message.strip()
                        message = message[0].upper() + message[1:]

                        for i in message_full.split():
                            if i.startswith("@"):
                                message_full = message_full.replace(i, "")
                        message_full = message_full.strip()
                        message_full = message_full[0].upper(
                        ) + message_full[1:]

                        try:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - replied to a tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                            except:
                                api.create_tweet(
                                    text=f"❗️{author} - replied to a tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                        except:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - replied to a tweet.\n", quote_tweet_id=id_auth)
                            except ValueError:
                                print("Could not create tweet.")

                # Quote - person from list

                else:
                    author = status.user.name
                    author_screen_name = f"@{status.user.screen_name}"
                    id_auth = status.id

                    message = message.replace("@", "")

                    message_get = api.get_tweet(id=id_auth)
                    message_full = message_get.data["text"]
                    message_full = message_full.replace("@", "")

                    try:
                        first_list_quoted = status.quoted_status.user
                        first_author_name = f"{first_list_quoted.name}"
                        first_author_screen_name = f"@{first_list_quoted.screen_name}"
                    except ValueError:
                        print("Transform - Error")
                    if author_screen_name == first_author_screen_name:
                        try:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted own tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                            except:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted own tweet.\n🗨️ Text: „{message}”", quote_tweet_id=id_auth)
                        except:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted own tweet.\n", quote_tweet_id=id_auth)
                            except ValueError:
                                print("Could not create tweet.")
                    else:
                        try:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted {first_author_name} tweet.\n🗨️ Text: „{message_full}”", quote_tweet_id=id_auth)
                            except:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted {first_author_name} tweet.\n🗨️ Text: „{message}”", quote_tweet_id=id_auth)
                        except:
                            try:
                                api.create_tweet(
                                    text=f"❗️{author} - quoted {first_author_name} tweet.\n", quote_tweet_id=id_auth)
                            except ValueError:
                                print("Could not create tweet.")
        except:
            print("Failed status")


api = tweepy.Client(bearer_token=br_token, consumer_key=api_key,
                    consumer_secret=api_sec_key, access_token=ac_key, access_token_secret=ac_sec_key)

api_stream = id_printer(api_key, api_sec_key, ac_key, ac_sec_key)

tw_ids = search.persons
print(tw_ids)
api_stream.filter(follow=tw_ids)
