#!/usr/local/bin/python3
# __*_ coding: utf-8 _*_
# follower choice  method class
import json
import pytwitter
import sys
from datetime import date


class FollowerConditionScreening:
    """
    user_object:
        create_date
        tweet_count
        follower_count
    """

    def get_key_from_value(self, dict_object, value_que):
        """
        value_queを含む持つkeyのリストを返す
        :param dict_object:
        :param value_que:
        :return: key
        """
        keys_list = [key for key, value in dict_object.items() if value_que in value]
        if keys_list[0]:
            return keys_list
        else:
            return None

    def get_user_create_date(self, user_id, value):
        """
        指定した
        :param user_id:
        :param value:
        :return: datetime
        """



    user_object = {}
    with open('example/user_object.json', 'r', encoding='utf-8') as f:
        user_object = json.load(f)
        print(user_object['id'])


if __name__ == "__main__":
    pass
