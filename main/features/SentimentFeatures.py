from utils import utils
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()


def get_hyperbolic_words_feature(connection, post):
    """
    Checks if there are any hyperbolic words in the provided
    post's texts and article's title. NOTE! This needs the NLP Stanford
    server to be up and running.
    :param connection: the connection to the stanford local server
    :param post: the current post
    :return: a list with 1s or 0s based on whether the post text/article title
    contains at least one hyperbolic word or not
    """
    post_text = utils.title(post)
    article_title = utils.article(post)

    found_in_post_text = has_hyperbolic_words(connection, post_text)
    found_in_article_title = has_hyperbolic_words(connection, article_title)

    return [found_in_post_text, found_in_article_title]


def has_hyperbolic_words(connection, post_field):
    """
    Splits the post_field parameter into tokens and for each of them,
    invokes a call to the StanfordNLP server in order to identify if the token
    is a hyperbolic word
    :param connection: the connection to the stanford local server
    :param post_field: the field to be checked
    :return: 1 if the post_field contains hyperbolic words, else 0
    """
    # If list extract the element into a string
    if isinstance(post_field, list):
        post_field = post_field[0]
    post_title_tokens = post_field.split()
    found = 0
    for token in post_title_tokens:
        res = connection.annotate(token, properties={
            'annotators': 'sentiment',
            'outputFormat': 'json',
            'timeout': 10000})
        for s in res["sentences"]:
            sentiment_value = s["sentimentValue"]
            if int(sentiment_value) == 4 or int(sentiment_value) == 0:  # 4: very positive 0: very negative
                found = 1
                break
    return found


def get_sentiment_polarity_feature(post):
    """
    Calculates the compound score of the post's text and the
    article's title
    :param post: the current post
    :return: a list with the compound scores
    """
    post_text = utils.title(post)
    article_title = utils.article(post)

    # If list extract the element into a string
    if isinstance(post_text, list):
        post_text = post_text[0]
    if isinstance(article_title, list):
        article_title = article_title[0]

    scores_post_text = analyser.polarity_scores(post_text)
    scores_article_title = analyser.polarity_scores(article_title)
    return [scores_post_text["compound"], scores_article_title["compound"]]
