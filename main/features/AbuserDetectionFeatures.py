from datetime import datetime
from utils import utils
import pytz

# TODO: maybe change that to a module
class AbuserDetectionFeatures:
    def __init__(self):
        print("Abuser detection features")

    def get_no_signs(self, post):
        signs = 0
        if isinstance(post, str):
            # string case
            signs = post.count('@')
        else:
            # list case
            for item in post:
                signs += item.count('@')
        return signs

    def get_no_hashtags(self, post):
        hashtags = 0
        if isinstance(post, str):
            # string case
            hashtags = post.count('#')
        elif isinstance(post, list):
            # list case
            for item in post:
                hashtags += item.count('#')
        return hashtags

    def get_no_exclamations(self, post):
        exclam = 0
        if isinstance(post, str):
            # string case
            exclam = post.count('!')
        elif isinstance(post, list):
            # list case
            for item in post:
                exclam += item.count('!')
        return exclam

    def get_no_questionmarks(self, post):
        questions = 0
        if isinstance(post, str):
            # string case
            questions = post.count('?')
        elif isinstance(post, list):
            # list case
            for item in post:
                questions += item.count('?')
        return questions

    def get_no_abbreviations(self, post):
        abbreviations = 0
        if isinstance(post, str):
            # string case
            abbreviations = post.count("'")
        elif isinstance(post, list):
            # list case
            for item in post:
                abbreviations += item.count("'")
        return abbreviations

    def get_no_ellipses(self, post):
        ellipses = 0
        if isinstance(post, str):
            # string case
            ellipses = post.count('...')
        elif isinstance(post, list):
            # list case
            for item in post:
                ellipses += item.count('...')
        return ellipses

    def get_no_dots(self, post):
        dots = 0
        if isinstance(post, str):
            # string case
            dots = post.count('.')
        elif isinstance(post, list):
            # list case
            for item in post:
                dots += item.count('.')
        return dots

    def get_begins_with_interrogative(self, post):
        interrogative = 0
        if isinstance(post, str):
            # string case
            if post.startswith('Who') or post.startswith('What') or post.startswith('When') or post.startswith('Where') \
                    or post.startswith('Why') or post.startswith('How'):
                interrogative = 1
        elif isinstance(post, list):
            # list case
            for item in post:
                if item.startswith('Who') or item.startswith('What') or item.startswith('When') or item.startswith('Where') \
                        or item.startswith('Why') or item.startswith('How'):
                    interrogative = 1
                    break
        return interrogative

    def get_begins_with_number(self, post):
        number = 0
        if isinstance(post, str):
            # string case
            if post[0].isdigit():
                number = 1
        elif isinstance(post, list):
            # list case
            for item in post:
                if item[0].isdigit():
                    number = 1
                    break
        return number

    def get_no_excl_quest(self, post):
        excl_quest = 0
        if isinstance(post, str):
            # string case
            excl_quest = post.count('!?')
        elif isinstance(post, list):
            # list case
            for item in post:
                excl_quest += item.count('!?')
        return excl_quest

    def get_no_punctuation(self, post):
        punctuation = 0
        if isinstance(post, str):
            # string case
            punctuation = post.count('?') + post.count(',') + post.count(':') + post.count('...')
        elif isinstance(post, list):
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

    def get_post_creation_hour(self, post):
        post_timestamp = datetime.strptime(utils.timestamp(post), '%a %b %d %H:%M:%S %z %Y')
        timestamp_hour = post_timestamp.time().hour
        for i in range(0, 24):
            if i <= timestamp_hour < i+1:
                hour = i + 1
                return hour
