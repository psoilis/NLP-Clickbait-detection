import re
from utils import utils, NgramUtils

# List of common clickbait phrases
clickbait_phrases = ["A Single", "Absolutely", "Amazing", "Awesome", "Best", "Breathtaking",
                     "But what happened next", "Can change your life", "Can't Even Handle",
                     "Can't Handle", "Cannot Even Handle", "Doesn't want you to see", "Epic",
                     "Everything You Need To Know", "Gasp-Worthy", "Go Viral", "Greatest", "Incredible",
                     "Infuriate", "Literally", "Mind Blowing", "Mind-Blowing", "Mind BLOWN", "Mind Blown",
                     "Need To Visit Before You Die", "Nothing Could Prepare Me For", "Of All Time", "Of All Time",
                     "Of All-Time", "OMG", "One Weird Trick", "Perfection", "Priceless", "Prove", "Right Now",
                     "Scientific Reasons", "Shocked", "Shocking", "Simple Lessons",
                     "Stop What You’re Doing", "Stop What You're Doing", "TERRIFYING", "Terrifying",
                     "That Will Make You Rethink", "The World's Best", "This Is What Happens",
                     "Totally blew my mind", "Unbelievable", "Unimaginable", "WHAT?", "Whoa", "WHOA",
                     "Whoah", "Will Blow Your Mind", "Will Change Your Life Forever", "Won the Internet",
                     "Wonderful", "Worst", "Wow", "WOW", "You Didn't Know Exist", "You Didn't Know Existed",
                     "You Didn’t Know Exist", "You Didn’t Know Existed", "You Won't Believe", "You Won’t Believe",
                     "You Wont Believe", "Have To See To Believe"]

# List of slang words
slang_words = ["3cool5u", "420", "afaik", "afk", "asl", "atm", "atw", "ayy", "bae", "bb", "bbiab", "bbl", "bbs",
               "bc", "bf", "bff", "bork", "brb", "btw", "cba", "convo", "cp", "cya", "dank", "dc", "dem feels", "dw",
               "e2e", "fml", "FOMO", "FTFY", "ftl", "ftw", "fwiw", "fyi", "g2g", "g4u", "gf", "gg", "goml", "gr8",
               "gratz", "gtfo", "guiz", "hbu", "hru", "ianadb", "ianalb", "ianap", "idc", "idgaf", "idk", "iirc", "ik",
               "ikr", "ily", "inb4", "irl", "jfc", "jk", "John Cena", "JOHN CENA", "js", "k", "kappa", "kek", "kms",
               "kthx", "l8r", "leet", "lmao", "lmk", "lol", "LPT", "lrl", "lrn2", "m8", "maga", "mfw", "mrw", "nerf",
               "ngl", "nm", "nmu", "noob", "nu", "nvm", "ofc", "omf", "omg", "omw", "ooc", "op", "OP", "orly", "pepe",
               "pleb", "pleb tier", "plz", "pron", "pwned", "REEEEEEEE", "rekt", "rickroll", "rip", "rly", "rms",
               "rofl", "rotflol", "rtfm", "rude", "shank", "smd", "smh", "soz", "swag", "tbf", "tbh", "tbt", "TIFU",
               "tf", "tfw", "thx", "tide", "TIL", "tl;dr", "tmw", "tolo", "topkek", "ty", "uwotm8", "w00t", "wb",
               "wot", "wtb", "wtf", "wtg", "wts", "wuu2", "yarly", "ymmv", "yolo", "yw"]

# Dictionary containing the initialized to zero n-gram feature vectors for n in [1,3]
ngram_corpus = {1: {}, 2: {}, 3: {}}


def get_no_of_characters_features(post):
    """
    Calculates the "Number of characters" features. 4 features
    are calculated in total
    :return: a list that contains the features
    """
    f1 = utils.len_characters(utils.title(post))
    f2 = utils.len_characters(utils.article(post))
    f3 = utils.len_characters(utils.description(post))
    f4 = utils.len_characters(utils.keywords(post))
    return [f1, f2, f3, f4]


def get_diff_between_no_of_characters_features(post):
    """
    Calculates the "Difference between number of chars" features.
    6 features are calculated in total
    :return: a list that contains the features
    """
    post_title_len = utils.len_characters(utils.title(post))
    article_title_len = utils.len_characters(utils.article(post))
    article_desc_len = utils.len_characters(utils.description(post))
    article_keywords_len = utils.len_characters(utils.keywords(post))

    lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

    features_lst = get_difference_features_list(lst)
    return features_lst


def get_no_of_characters_ratio_features(post):
    """
    Calculates the "Number of characters ratio". 6 features
    are calculated in total
    :return: a list that contains the features
    """
    post_title_len = utils.len_characters(utils.title(post))
    article_title_len = utils.len_characters(utils.article(post))
    article_desc_len = utils.len_characters(utils.description(post))
    article_keywords_len = utils.len_characters(utils.keywords(post))

    lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

    features_lst = get_ratio_features_list(lst)
    return features_lst


def get_no_of_words_features(post):
    """
    Calculates the "Number of words" features. 4 features
    are calculated in total
    :return: a list that contains the features
    """
    f1 = utils.len_words(utils.title(post))
    f2 = utils.len_words(utils.article(post))
    f3 = utils.len_words(utils.description(post))
    f4 = utils.len_words(utils.keywords(post))
    return [f1, f2, f3, f4]


def get_diff_between_no_of_words_features(post):
    """
    Calculates the "Difference between number of words" features.
    6 features are calculated in total
    :return: a list that contains the features
    """
    post_title_len = utils.len_words(utils.title(post))
    article_title_len = utils.len_words(utils.article(post))
    article_desc_len = utils.len_words(utils.description(post))
    article_keywords_len = utils.len_words(utils.keywords(post))

    lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

    features_lst = get_difference_features_list(lst)
    return features_lst


def get_no_of_words_ratio_features(post):
    """
    Calculates the "Number of words ratio". 6 features
    are calculated in total
    :return: a list that contains the features
    """
    post_title_len = utils.len_words(utils.title(post))
    article_title_len = utils.len_words(utils.article(post))
    article_desc_len = utils.len_words(utils.description(post))
    article_keywords_len = utils.len_words(utils.keywords(post))

    lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

    features_lst = get_ratio_features_list(lst)
    return features_lst


def get_common_clickbait_phrases_feature(post):
    """
    Checks whether the post's text and article's title contain
    common words/phrases
    :param post: the current post
    :return: a list of 0s, 1s indicating whether the fields contain
    common words/phrases
    """
    post_text = utils.title(post)
    article_title = utils.article(post)

    found_in_post_text = has_common_phrases(post_text)
    found_in_article_title = has_common_phrases(article_title)

    return [found_in_post_text, found_in_article_title]


def has_common_phrases(post_field):
    """
    Checks if the provided post_field contains common words/phrases
    :param post_field: the field to be checked
    :return: 1 if the post_field contains common words/phrases, else 0
    """
    found = 0
    for phrase in clickbait_phrases:
        if phrase in post_field:
            found = 1
            break
    return found


def get_slang_words_feature(post):
    """
    Checks whether the post's text and article's title contain
    slang words
    :param post: the current post
    :return: a list of 0s, 1s indicating whether the fields contain
    slang words
    """
    post_text = utils.title(post)
    article_title = utils.article(post)

    found_in_post_text = has_slang_words(post_text)
    found_in_article_title = has_slang_words(article_title)

    return [found_in_post_text, found_in_article_title]


def has_slang_words(post_field):
    """
    Checks if the provided post_field contains hyperbolic words
    :param post_field: the field to be checked
    :return: 1 if the post_field contains slang words, else 0
    """
    # If list extract the element into a string
    if isinstance(post_field, list):
        post_field = post_field[0]
    found = 0
    for phrase in slang_words:
        result = re.search(r'\b' + phrase + '\W', post_field)
        if result:
            found = 1
            break
    return found


def get_ngram_counts(post, n, l_t, u_t):
    """
    Calculates the ngram features of the post

    :arg post: The post that we want to extract the features from
    :arg n: The n in n-gram
    :arg l_t: The lower threshold that removes n-grams with lower counts than the threshold in the dataset
    :arg u_t: The upper threshold that removes n-grams with higher counts than the threshold  in the dataset

    :return: the n gram feature vector of the post
    """
    # If the n-gram corpus hasn't benn yet initialized initialize it
    if not ngram_corpus[n]:
        ngram_corpus[n] = NgramUtils.get_ngram_corpus(n, l_t, u_t).copy()

    # Return the n-gram feature vector of the post
    return NgramUtils.get_ngram_feature_vector(post, n, ngram_corpus[n])


def get_title_patterns(comp):
    """
    Function that checks if the following patterns exist in our content element
    Pattern 1: Number + Noun Phrase + Verb
    Pattern 2: Number + Noun Phrase + the word "that"
    (check utils.py for additional information)
    """
    return utils.article_title_patterns(comp)


def get_POS_counts(comp):
    """
    Function that returns the POS tag count of the specified content element
    (check utils.py for additional information)
    """
    return utils.POS_counts(comp)


def get_det_poses(comp):
    """
    Function that determines if possessives and determiners exist in the specified content
    (check utils.py for additional information)
    """
    return utils.determiners_possessives_bool(comp)


def get_difference_features_list(lst):
    features_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] != -1 and lst[j] != -1:
                features_lst.append(abs(lst[i] - lst[j]))
            else:
                features_lst.append(-1)
    return features_lst


def get_ratio_features_list(lst):
    features_lst = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] != -1 and lst[j] != -1:
                features_lst.append(abs(float(lst[i]) / lst[j]))
            else:
                features_lst.append(-1)
    return features_lst
