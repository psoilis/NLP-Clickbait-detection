def img(post):
    return "fix"


def ocr(post):
    return "fix"


def title(post):
    # returns the post's title
    return post["postText"]


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
    return "fix"


def lang_dict_informal(content):
    return "fix"
