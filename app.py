import tweepy
import search
from key import api_key, api_sec_key, ac_key, ac_sec_key

class id_printer(tweepy.Stream):

    def on_status(self, status):
        if status.user.id_str in york:
            message = status.text
            status_quote = status.is_quote_status            
            if message.startswith("RT "):
                author = status.user.name
                author_screen_name = f"@{status.user.screen_name}"
                id_auth = status.id
                print(id_auth)
                dict_post = status.entities
                first_author_dict_value = dict_post["user_mentions"]
                first_author_list_value = first_author_dict_value[0]
                first_author_screen_name = f"@{first_author_list_value['screen_name']}"
                api2.update_status(status=f"❗️{author}({author_screen_name}) - Retweetował post użytkownika {first_author_screen_name}.", in_reply_to_status_id=id_auth)
                        
            elif status_quote == False:
                if status.in_reply_to_status_id == None:
                    author = status.user.name
                    author_screen_name = f"@{status.user.screen_name}"
                    id_auth = status.id
                    api2.update_status(status=f"❗️{author}({author_screen_name}) - dodał tweeta.\n🗨️ Treść: \„{message}\”", in_reply_to_status_id=id_auth)              
                    print("Tweet")

                else:
                    author = status.user.name
                    author_screen_name = f"@{status.user.screen_name}"
                    id_auth = status.id  
                    if status.in_reply_to_status_id != 1463184024659234820:
                        api2.update_status(status=f"❗️{author}({author_screen_name}) - skomentował post pisząc do @{status.in_reply_to_screen_name}.\n🗨️ Treść: \„{message}\”", in_reply_to_status_id=id_auth)              
                        print("Komentarz")
                    else:
                        print("Blokada komentarza do konta")
            else:
                author = status.user.name
                author_screen_name = f"@{status.user.screen_name}"
                id_auth = status.id
                print(id_auth)
                try:
                    first_list_quoted = status.quoted_status.user
                    first_author_screen_name = f"@{first_list_quoted.screen_name}"
                except:
                    print("Error")
                if author_screen_name == first_author_screen_name:
                    try:
                        api2.update_status(status=f"❗️{author}({author_screen_name}) - cytuje samego siebie.\n🗨️ Treść: \„{message}\”", in_reply_to_status_id=id_auth)
                    except:
                        print("Error")
                else:
                    try:
                        api2.update_status(status=f"❗️{author}({author_screen_name}) - cytuje {first_author_screen_name}.\n🗨️ Treść: \„{message}\”", in_reply_to_status_id=id_auth)
                    except:
                        print("Error")


auth = tweepy.OAuthHandler(api_key, api_sec_key)
auth.set_access_token(ac_key, ac_sec_key)
api2 = tweepy.API(auth)

api = id_printer(api_key, api_sec_key, ac_key, ac_sec_key)

york = search.persons
print(york)
api.filter(follow=york)