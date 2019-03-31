from datetime import datetime
import pytz

# TODO: maybe change that to a module
class AbuserDetectionFeatures:
    def __init__(self):
        print("Abuser detection features")

    def get_no_signs(self, post):
        signs = 0
        if len(post) == 1:
            # string case
            signs = post[0].count('@')
        else:
            # list case
            for item in post:
                signs += item.count('@')
        return signs

    def get_no_hashtags(self, post):
        hashtags = 0
        if len(post) == 1:
            # string case
            hashtags = post[0].count('#')
        else:
            # list case
            for item in post:
                hashtags += item.count('#')
        return hashtags

    def get_no_punctuation(self, post):
        punctuation = 0
        if len(post) == 1:
            # string case
            punctuation = post[0].count('?') + post[0].count(',') + post[0].count(':') + post[0].count('...')
        else:
            # list case
            for item in post:
                punctuation += item.count('?') + item.count(',') + item.count(':') + item.count('...')
        return punctuation

    def get_no_keywords(self, article):
        keywords = 0
        # keywords = len(article) # if we count number of elements in list
        for item in article:
            keywords += len(item.split()) # if we count the number of all the words in the list
        return keywords

    def get_no_paragraphs(self, article):
        paragraphs = len(article)
        return paragraphs

    def get_no_captions(self, article):
        captions = len(article)
        return captions

    def get_post_longevity(self, post_timestamp):
        days = (datetime.now().replace(tzinfo=pytz.UTC) - post_timestamp).days # Post timestamp in UTC, Netherlands in UTC+1
        return days

    def get_post_creation_hour(self, post_timestamp):
        timestamp_hour = post_timestamp.time().hour
        for i in range(0, 24):
            if i <= timestamp_hour < i+1:
                hour = i + 1
                return hour
