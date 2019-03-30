import pytesseract
from PIL import Image
from PyDictionary import PyDictionary
from nltk import word_tokenize, pos_tag


def img(post):

    pm = post["postMedia"]

    if pm is None:
        return None
    else:
        return Image.open(pm)


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

    return chars_len


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
    return words_len


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


def lang_dict_formal(content):

    wo = words(content)
    dictionary = PyDictionary()

    formal = []

    for w in wo:
        if dictionary.meaning(w) is not None:
            formal.append(w)

    return formal


def lang_dict_informal(content):

    wo = words(content)
    dictionary = PyDictionary()

    informal = []

    for w in wo:
        if dictionary.meaning(w) is None:
            informal.append(w)

    return informal


def determiners_possessives_bool(content):

    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    tagged_tokens = pos_tag(word_tokenize(text))

    d_flag = False
    p_flag = False

    for t in tagged_tokens:

        if d_flag and p_flag:
            # Early termination
            break

        if t[1] == "DT":
            # determiner
            d_flag = True
        elif t[1] == "PRP$":
            # possessives
            p_flag = True

    return d_flag, p_flag

