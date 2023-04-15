import json

# loading in followers and following list
followers_json = json.load(open("followers.json"))
following_json = json.load(open("following.json"))

followers_cleaned = set()
following_cleaned = set()

# collect all followers to set
for person in followers_json:
    followers_cleaned.add(person["string_list_data"][0]['value'] + ":" + person["string_list_data"][0]['href'])

# collect all following to set
for person in following_json["relationships_following"]:
    following_cleaned.add(person["string_list_data"][0]['value'] + ":" + person["string_list_data"][0]['href'])

# people not following back
not_following_me = following_cleaned - followers_cleaned

# fake friends 🗣️
for fake_friend in not_following_me:
    print(fake_friend)

# stats
print("Number of Folowers:", len(followers_cleaned))
print("Number of Folowing:", len(following_cleaned))