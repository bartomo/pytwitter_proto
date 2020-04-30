##!/usr/local/bin/python3
# _*_ coding: utf-8 _*
# _ Python Api method class
import sys
import json
import twitter
# import requests
# import requests_oauthlib
from t import ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET

api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)


class PyTwitter:
    """
    TwitterAPI method component
    follower_list
    user_object
    """

    def get_tweet(self, api=None, screen_name=None):
        timeline = api.GetUserTimeline(screen_name=screen_name, count=200)
        earliest_tweet = min(timeline, key=lambda x: x.id).id
        print('getting tweet before:', earliest_tweet)

        while True:
            tweets = api.GetUserTimeline(
                screen_name = screen_name, max_id=earliest_tweet, count=200
            )
            new_earliest = min(tweets, key=lambda x: x.id).id

            if not tweets or new_earliest == earliest_tweet:
                break
            else:
                earliest_tweet = new_earliest
                print("getting tweet before : ", earliest_tweet)
                timeline += tweets
        return timeline

    def get_user_object(self, api=None, screen_name=None):
        user_object = api.GetUser(screen_name=screen_name)
        print('getting user_object : ', screen_name)
        return user_object

    def get_followers_ids(self, api=None, screen_name=None):
        """

        :param api:
        :param screen_name:
        :return:list
        """
        followers_ids = api.GetFollowerIDs(screen_name=screen_name)
        print('getting followers_ids:', followers_ids[:10])
        return followers_ids


if __name__ == "__main__":
    ins_pytwitter = PyTwitter()
    screen_name = sys.argv[1]
    timeline = ins_pytwitter.get_tweet(api=api, screen_name=screen_name)
    user = ins_pytwitter.get_user_object(api=api, screen_name=screen_name)
    followers = ins_pytwitter.get_followers_ids(api=api, screen_name=screen_name)

    with open('example/timeline.json', 'w+', encoding='utf-8') as f:
        for tweet in timeline:
            f.write(json.dumps(tweet._json, indent=4, ensure_ascii=False))
            f.write('\n')

    with open('example/user_object.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(user._json, indent=4, ensure_ascii=False))
        f.write('\n')

    with open('example/user_followers_ids.json', 'w+', encoding='utf-8') as f:
        f.write(json.dumps(followers, indent=4, ensure_ascii=False))
        f.write('\n')
