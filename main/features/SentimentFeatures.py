from main.utils import utils
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


def get_hyperbolic_words_feature(connection, post):
    """
    Checks if there are any hyperbolic words in the provided
    post's title. NOTE! This needs the NLP Stanford server to be
    up and running.
    :param connection: the connection to the stanford local server
    :param post: the current post
    :return: 1 or 0 based on whether the post title contains
    at least one hyperbolic word or not
    """
    post_title = utils.title(post)
    post_title_tokens = post_title.split()

    found = 0
    for token in post_title_tokens:
        res = connection.annotate(token, properties={
                                   'annotators': 'sentiment',
                                   'outputFormat': 'json',
                                   'timeout': 1000})
        for s in res["sentences"]:
            sentiment_value = s["sentimentValue"]
            if int(sentiment_value) == 4:   # 4: very positive
                found = 1
                break

    return found


def get_sentiment_polarity_feature(post):
    """
    Calculates the compound score of the post's title
    :param post: the current post
    :return: the compound score
    """
    post_title = utils.title(post)

    scores = analyser.polarity_scores(post_title)
    return scores["compound"]
