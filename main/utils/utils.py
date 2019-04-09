from nltk import word_tokenize, pos_tag
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


def get_label_dict():
    labels = {}
    with open('dataset/truth.jsonl', 'rb') as label_file:
        for data in json_lines.reader(label_file):
            if truth_label(data) == 'no-clickbait':
                labels[post_id(data)] = 0
            elif truth_label(data) == 'clickbait':
                labels[post_id(data)] = 1
    return labels


def determiners_possessives_bool(content):
    """
    Function that determines if possessives and determiners exist in the specified content

    :arg content: The content element that we check

    :return d_flag: 1 if determiners exist returns 0 otherwise
    :return p_flag: 1 if possessives exist returns 0 otherwise
    """

    # Check if the content element is a list or a string and append it to the variable text as String
    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    # Get the string's POS tags
    tagged_tokens = pos_tag(word_tokenize(text.lower()))

    # Initialize the tags
    d_flag = 0
    p_flag = 0

    # For very POS tag
    for t in tagged_tokens:

        # If both flags are 1 then break for early termination
        if (d_flag + p_flag) == 2:
            break

        # If the token is tagged as a determiner set the determiner flag to 1
        if t[1] == "DT":
            d_flag = 1
        # If the token is tagged as a possessive set the possessive flag to 1
        elif t[1] == "PRP$" or t[1] == "PRP":
            p_flag = 1

    # Return both flags
    return d_flag, p_flag


def article_title_patterns(content):
    """
    Function that checks if the following patterns exist in our content element
    Pattern 1: Number + Noun Phrase + Verb
    Pattern 2: Number + Noun Phrase + the word "that"

    :arg content: The content element that we check

    :return nnpv: 1 if Pattern 1 exists returns 0 otherwise
    :return nnpt: 1 if Pattern 2 exists returns 0 otherwise
    """

    # Check if the content element is a list or a string and append it to the variable text as String
    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    # Get the string's POS tags
    tagged_tokens = pos_tag(word_tokenize(text.lower()))

    # If we get an empty list return False on both flags
    if len(tagged_tokens) == 0:
        return False, False

    # If the pattern doesn't starat with a number return False on both flags
    if tagged_tokens[0][1] != "CD":
        return False, False

    # Initialize the flags
    nnpv = False
    nnpt = False

    # If the Noun phrase has occurred
    np = False

    # For every token
    for i in range(1, len(tagged_tokens)):

        # If we encounter the noun in the phrase
        if "NN" in tagged_tokens[i][1]:
            np = True
        # If we don't encounter the noun in the phrase and it wasn't found previously
        if tagged_tokens[i][1] not in "NN" and not np:
            return False, False

        # If we encounter the verb
        if tagged_tokens[i][1] in "VB" and np:
            nnpv = True

        # If we encounter the word "that"
        if tagged_tokens[i][0] == "that" and np:
            nnpt = True

    # Return both flags
    return nnpv, nnpt


def POS_counts(content):
    """
    Function that returns the POS tag count of the specified content element

    :arg content: The content element that we check

    :return cdict : The dictionary that contains the counts
    """

    # Check if the content element is a list or a string and append it to the variable text as String
    text = ""

    if isinstance(content, list):
        for t in content:
            text += t + " "
    else:
        text = content

    # Initialize the dictionary with only the relevant POS tags with 0 values
    cdict = {"NNP": 0, "IN": 0, "WRB": 0, "NN": 0, "PRP": 0, "VBZ": 0, "PRP$": 0, "VBD": 0, "VBP": 0,
             "WP": 0, "DT": 0, "POS": 0, "WDT": 0, "RB": 0, "RBS": 0, "VBN": 0}

    # For every token
    for t in text.split(" "):

        # Get the token's tag
        tag = pos_tag(word_tokenize(t))

        # If the list wasn't empty
        if len(tag) != 0:

            # Increment the dictionary
            if tag[0][1] in cdict.keys():
                cdict[tag[0][1]] += 1
            # Add the plurals to the normal count
            elif tag[0][1] == "NNPS":
                cdict["NNP"] += 1
            elif tag[0][1] == "NNS":
                cdict["NN"] += 1

    # Return the dictionary with the POS tag counts
    return cdict
