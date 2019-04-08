from nltk import word_tokenize, pos_tag
from collections import Counter
import json_lines


def img(post):

    pm = post["postMedia"]

    if not pm:
        return None
    else:
        return 1


def post_id(post):
    # returns post's id
    return post["id"]


def title(post):
    # returns the post's title
    return post["postText"]


def timestamp(post):
    # returns the post's timestamp
    return post["postTimestamp"]


def article(post):
    # returns the article's title
    return post["targetTitle"]


def description(post):
    # returns the target article's description
    return post["targetDescription"]


def keywords(post):
    # returns the target article's keywords
    k_words = post["targetKeywords"]
    if len(k_words) == 0:
        return []
    else:
        return k_words.split(",")


def paragraphs(post):
    # returns the target article's title
    return post["targetParagraphs"]


def captions(post):
    # returns the target article's captions
    return post["targetCaptions"]


def truth_label(post):
    # returns the post label from the truth file
    return post['truthClass']


def len_characters(content):
    # returns the content's number of characters (-1 if empty)
    chars_len = - 1
    if len(content) != 0:
        if isinstance(content, list):
            # list case
            chars_sum = 0
            for element in content:
                chars_sum = chars_sum + len(element)
            chars_len = chars_sum / float(len(content))
        else:
            # string case
            chars_len = len(content)

    return chars_len if chars_len != 0 else -1


def len_words(content):
    # returns the content's number of words (-1 if empty)
    words_len = - 1
    if len(content) != 0:
        if isinstance(content, list):
            # list case
            words_sum = 0
            for element in content:
                words = element.split(" ")
                words_sum = words_sum + len(words)
                words_len = words_sum / float(len(content))
        else:
            # string case
            words = content.split(" ")
            words_len = len(words)
    return words_len if words_len != 0 else -1


def words(content):
    # returns the content's words
    words_lst = []
    if isinstance(content, list):
        # list case
        for element in content:
            words = element.split(" ")
            words_lst.extend(words)
    else:
        # string case
        words_lst = content.split(" ")

    return words_lst


def determiners_possessives_bool(content):

    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    tagged_tokens = pos_tag(word_tokenize(text.lower()))

    d_flag = 0
    p_flag = 0

    for t in tagged_tokens:

        if d_flag and p_flag:
            # Early termination
            break

        if t[1] == "DT":
            # determiner
            d_flag = 1
        elif t[1] == "PRP$" or t[1] == "PRP":
            # possessives
            p_flag = 1

    return d_flag, p_flag


def article_title_patterns(content):

    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    tagged_tokens = pos_tag(word_tokenize(text.lower()))

    if tagged_tokens[0][1] != "CD":
        return False, False

    nnpv = False
    nnpt = False

    np = False

    for i in range(1, len(tagged_tokens)):

        if "NN" in tagged_tokens[i][1]:
            np = True

        if tagged_tokens[i][1] not in "NN" and not np:
            return False, False

        if tagged_tokens[i][1] in "VB" and np:
            nnpv = True

        if tagged_tokens[i][0] == "that" and np:
            nnpt = True

    return nnpv, nnpt


def POS_counts(content):

    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    cdict = {"NNP": 0, "IN": 0, "WRB": 0, "NN": 0, "PRP": 0, "VBZ": 0, "PRP$": 0, "VBD": 0, "VBP": 0,
             "WP": 0, "DT": 0, "POS": 0, "WDT": 0, "RB": 0, "RBS": 0, "VBN": 0}

    for t in text.split(" "):

        tag = pos_tag(word_tokenize(t))

        if len(tag) != 0:

            if tag[0][1] in cdict.keys():
                cdict[tag[0][1]] += 1
            elif tag[0][1] == "NNPS":
                cdict["NNP"] += 1
            elif tag[0][1] == "NNS":
                cdict["NN"] += 1

    return cdict

def get_label_dict():
    labels = {}
    with open('dataset/truth.jsonl', 'rb') as label_file:
        for data in json_lines.reader(label_file):
            if truth_label(data) == 'no-clickbait':
                labels[post_id(data)] = 0
            elif truth_label(data) == 'clickbait':
                labels[post_id(data)] = 1
    return labels
