from datetime import datetime
from utils import utils


def get_no_signs(content):
    """
    Counts the number of "@" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    signs = 0
    if isinstance(content, str):
        # string case
        signs = content.count('@')
    else:
        # list case
        for item in content:
            signs += item.count('@')
    return signs


def get_no_hashtags(content):
    """
    Counts the number of "#" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    hashtags = 0
    if isinstance(content, str):
        # string case
        hashtags = content.count('#')
    elif isinstance(content, list):
        # list case
        for item in content:
            hashtags += item.count('#')
    return hashtags


def get_no_exclamations(content):
    """
    Counts the number of "!" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    exclam = 0
    if isinstance(content, str):
        # string case
        exclam = content.count('!')
    elif isinstance(content, list):
        # list case
        for item in content:
            exclam += item.count('!')
    return exclam


def get_no_question_marks(content):
    """
    Counts the number of "?" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    questions = 0
    if isinstance(content, str):
        # string case
        questions = content.count('?')
    elif isinstance(content, list):
        # list case
        for item in content:
            questions += item.count('?')
    return questions


def get_no_abbreviations(content):
    """
    Counts the number of "'" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    abbreviations = 0
    if isinstance(content, str):
        # string case
        abbreviations = content.count("'")
    elif isinstance(content, list):
        # list case
        for item in content:
            abbreviations += item.count("'")
    return abbreviations


def get_no_ellipses(post):
    """
    Counts the number of "..." in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    ellipses = 0
    if isinstance(post, str):
        # string case
        ellipses = post.count('...')
    elif isinstance(post, list):
        # list case
        for item in post:
            ellipses += item.count('...')
    return ellipses


def get_no_dots(content):
    """
    Counts the number of "." in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    dots = 0
    if isinstance(content, str):
        # string case
        dots = content.count('.')
    elif isinstance(content, list):
        # list case
        for item in content:
            dots += item.count('.')
    return dots


def get_begins_with_interrogative(content):
    """
    Check if interrogatives exist in the provided content
    :param content: the passed content (e.g. post_text)
    :return: 1 if found, else 0
    """
    interrogative = 0
    if isinstance(content, str):
        # string case
        if content.startswith('Who') or content.startswith('What') or content.startswith('When') or content.startswith('Where') \
                or content.startswith('Why') or content.startswith('How'):
            interrogative = 1
    elif isinstance(content, list):
        # list case
        for item in content:
            if item.startswith('Who') or item.startswith('What') or item.startswith('When') or item.startswith('Where') \
                    or item.startswith('Why') or item.startswith('How'):
                interrogative = 1
                break
    return interrogative


def get_begins_with_number(content):
    """
    Check if the provided content begins with a number
    :param content: the passed content (e.g. post_text)
    :return: 1 if found, else 0
    """
    number = 0
    if isinstance(content, str):
        # string case
        if content[0].isdigit():
            number = 1
    elif isinstance(content, list):
        # list case
        for item in content:
            if len(item) != 0 and item[0].isdigit():
                number = 1
                break
    return number


def get_no_excl_quest(content):
    """
    Counts the number of "!?" in the provided content
    :param content: the passed content (e.g. post_text)
    :return: the calculated count
    """
    excl_quest = 0
    if isinstance(content, str):
        # string case
        excl_quest = content.count('!?')
    elif isinstance(content, list):
        # list case
        for item in content:
            excl_quest += item.count('!?')
    return excl_quest


def get_post_creation_hour(post):
    """
    Calculates the creation hour of the post
    :param post: the current post
    :return: returns the calculated hour
    """
    post_timestamp = datetime.strptime(utils.timestamp(post), '%a %b %d %H:%M:%S %z %Y')
    timestamp_hour = post_timestamp.time().hour
    for i in range(0, 24):
        if i <= timestamp_hour < i+1:
            hour = i + 1
            return hour
