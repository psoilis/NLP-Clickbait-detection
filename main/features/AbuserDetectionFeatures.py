from datetime import datetime
from utils import utils


def get_no_signs(post):
    signs = 0
    if isinstance(post, str):
        # string case
        signs = post.count('@')
    else:
        # list case
        for item in post:
            signs += item.count('@')
    return signs


def get_no_hashtags(post):
    hashtags = 0
    if isinstance(post, str):
        # string case
        hashtags = post.count('#')
    elif isinstance(post, list):
        # list case
        for item in post:
            hashtags += item.count('#')
    return hashtags


def get_no_exclamations(post):
    exclam = 0
    if isinstance(post, str):
        # string case
        exclam = post.count('!')
    elif isinstance(post, list):
        # list case
        for item in post:
            exclam += item.count('!')
    return exclam


def get_no_questionmarks(post):
    questions = 0
    if isinstance(post, str):
        # string case
        questions = post.count('?')
    elif isinstance(post, list):
        # list case
        for item in post:
            questions += item.count('?')
    return questions


def get_no_abbreviations(post):
    abbreviations = 0
    if isinstance(post, str):
        # string case
        abbreviations = post.count("'")
    elif isinstance(post, list):
        # list case
        for item in post:
            abbreviations += item.count("'")
    return abbreviations


def get_no_ellipses(post):
    ellipses = 0
    if isinstance(post, str):
        # string case
        ellipses = post.count('...')
    elif isinstance(post, list):
        # list case
        for item in post:
            ellipses += item.count('...')
    return ellipses


def get_no_dots(post):
    dots = 0
    if isinstance(post, str):
        # string case
        dots = post.count('.')
    elif isinstance(post, list):
        # list case
        for item in post:
            dots += item.count('.')
    return dots


def get_begins_with_interrogative(post):
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


def get_begins_with_number(post):
    number = 0
    if isinstance(post, str):
        # string case
        if post[0].isdigit():
            number = 1
    elif isinstance(post, list):
        # list case
        for item in post:
            if len(item) != 0 and item[0].isdigit():
                number = 1
                break
    return number


def get_no_excl_quest(post):
    excl_quest = 0
    if isinstance(post, str):
        # string case
        excl_quest = post.count('!?')
    elif isinstance(post, list):
        # list case
        for item in post:
            excl_quest += item.count('!?')
    return excl_quest


def get_post_creation_hour(post):
    post_timestamp = datetime.strptime(utils.timestamp(post), '%a %b %d %H:%M:%S %z %Y')
    timestamp_hour = post_timestamp.time().hour
    for i in range(0, 24):
        if i <= timestamp_hour < i+1:
            hour = i + 1
            return hour
