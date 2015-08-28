# coding: utf-8

import requests
from firebase import firebase


class HackerNews(object):
    def __init__(self):
        self.firebase_app = firebase.FirebaseApplication('https://hacker-news.firebaseio.com', None)

    def get_top_stories(self):
        result = self.firebase_app.get('/v0/topstories', None)
        return result

    def get_story(self, code):
        result = self.firebase_app.get('/v0/item/{0}'.format(code), None)
        return result

class Reddit(object):
    def __init__(self):
        self.headers = { 'user-agent': 'woid/1.0' }

    def get_front_page_stories(self):
        r = requests.get('https://www.reddit.com/.json', headers=self.headers)
        result = r.json()
        return result