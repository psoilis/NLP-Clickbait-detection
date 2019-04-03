import re
from utils import utils, NgramUtils


# TODO: maybe change that to a module
class LinguisticAnalysisFeatures:

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

    slang_words = ["3cool5u", "420", "afaik", "afk", "asl", "atm", "atw", "ayy", "bae", "bb", "bbiab", "bbl", "bbs",
                    "bc", "bf", "bff", "bork", "brb", "btw", "cba", "convo", "cp", "cya", "dank", "dc", "dem feels", "dw",
                    "e2e", "fml", "FOMO", "FTFY", "ftl", "ftw", "fwiw", "fyi", "g2g", "g4u", "gf", "gg", "goml", "gr8", "gratz",
                    "gtfo", "guiz", "hbu", "hru", "ianadb", "ianalb", "ianap", "idc", "idgaf", "idk", "iirc", "ik", "ikr", "ily",
                    "inb4", "irl", "jfc", "jk", "John Cena", "JOHN CENA", "js", "k", "kappa", "kek", "kms", "kthx", "l8r", "leet",
                    "lmao", "lmk", "lol", "LPT", "lrl", "lrn2", "m8", "maga", "mfw", "mrw", "nerf", "ngl", "nm", "nmu", "noob",
                    "nu", "nvm", "ofc", "omf", "omg", "omw", "ooc", "op", "OP", "orly", "pepe", "pleb", "pleb tier", "plz", "pron",
                    "pwned", "REEEEEEEE", "rekt", "rickroll", "rip", "rly", "rms", "rofl", "rotflol", "rtfm", "rude", "shank", "smd",
                    "smh", "soz", "swag", "tbf", "tbh", "tbt", "TIFU", "tf", "tfw", "thx", "tide", "TIL", "tl;dr", "tmw", "tolo",
                    "topkek", "ty", "uwotm8", "w00t", "wb", "wot", "wtb", "wtf", "wtg", "wts", "wuu2", "yarly", "ymmv", "yolo", "yw"]

    ngram_corpus = {}
    n = 0

    def __init__(self):
        print("Linguistic Analysis features")

    def get_no_of_characters_features(self, post):
        """
        Calculates the "Number of characters" features. 7 features
        are calculated in total
        :return: a list that contains the features
        """
        f1 = utils.len_characters(utils.title(post))
        f2 = utils.len_characters(utils.article(post))
        f3 = utils.len_characters(utils.description(post))
        f4 = utils.len_characters(utils.keywords(post))
        return [f1, f2, f3, f4]

    def get_diff_between_no_of_characters_features(self, post):
        """
        Calculates the "Difference between number of chars" features.
        21 features are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_characters(utils.title(post))
        article_title_len = utils.len_characters(utils.article(post))
        article_desc_len = utils.len_characters(utils.description(post))
        article_keywords_len = utils.len_characters(utils.keywords(post))

        lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

        features_lst = self.get_difference_features_list(lst)
        return features_lst

    # TODO: Should we include the other way around?
    def get_no_of_characters_ratio_features(self, post):
        """
        Calculates the "Number of characters ratio". 21 features
        are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_characters(utils.title(post))
        article_title_len = utils.len_characters(utils.article(post))
        article_desc_len = utils.len_characters(utils.description(post))
        article_keywords_len = utils.len_characters(utils.keywords(post))

        lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

        features_lst = self.get_ratio_features_list(lst)
        return features_lst

    def get_no_of_words_features(self, post):
        """
        Calculates the "Number of words" features. 7 features
        are calculated in total
        :return: a list that contains the features
        """
        f1 = utils.len_words(utils.title(post))
        f2 = utils.len_words(utils.article(post))
        f3 = utils.len_words(utils.description(post))
        f4 = utils.len_words(utils.keywords(post))
        return [f1, f2, f3, f4]

    def get_diff_between_no_of_words_features(self, post):
        """
        Calculates the "Difference between number of words" features.
        21 features are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_words(utils.title(post))
        article_title_len = utils.len_words(utils.article(post))
        article_desc_len = utils.len_words(utils.description(post))
        article_keywords_len = utils.len_words(utils.keywords(post))

        lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

        features_lst = self.get_difference_features_list(lst)
        return features_lst

    # TODO: Should we include the other way around?
    def get_no_of_words_ratio_features(self, post):
        """
        Calculates the "Number of words ratio". 21 features
        are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_words(utils.title(post))
        article_title_len = utils.len_words(utils.article(post))
        article_desc_len = utils.len_words(utils.description(post))
        article_keywords_len = utils.len_words(utils.keywords(post))

        lst = [post_title_len, article_title_len, article_desc_len, article_keywords_len]

        features_lst = self.get_ratio_features_list(lst)
        return features_lst

    def get_difference_features_list(self, lst):
        features_lst = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] != -1 and lst[j] != -1:
                    features_lst.append(abs(lst[i] - lst[j]))
                else:
                    features_lst.append(-1)
        return features_lst

    def get_ratio_features_list(self, lst):
        features_lst = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] != -1 and lst[j] != -1:
                    features_lst.append(abs(float(lst[i]) / lst[j]))
                else:
                    features_lst.append(-1)
        return features_lst

    def get_det_poses(self, post, comp):

        # TODO: modular? or for all example for title bellow
        if comp == "title":
            return utils.determiners_possessives_bool(utils.title(post))

    def get_common_clickbait_phrases_feature(self, post):
        post_title = utils.title(post)

        found = 0
        for phrase in self.clickbait_phrases:
            if phrase in post_title:
                found = 1
                break

        return found

    def get_slang_words_feature(self, post):
        post_title = utils.title(post)
        # If list extract the element into a string
        if isinstance(post_title, list):
            post_title = post_title[0]

        post_title = post_title.casefold()

        found = 0
        for phrase in self.slang_words:
            result = re.search(r'\b' + phrase + '\W', post_title)
            if result:
                found = 1
                break


        return found

    def get_title_patterns(self, post):
        return utils.article_title_patterns(utils.article(post))


    def get_POS_counts(self, post):
        return utils.POS_counts(utils.article(post))

    def get_ngram_counts(self, post, n, threshold):
        """
        :arg: post => the post that we want to extract the features from
        :arg: n => the n in n-gram
        Calculates the ngram features of the post
        :return: the n gram feature vector of the post
        """
        if not self.ngram_corpus or self.n != n:
            print('corpus')
            self.ngram_corpus = NgramUtils.get_ngram_corpus(n, threshold).copy()
            self.n = n
        return NgramUtils.get_ngram_feature_vector(post, self.n, self.ngram_corpus)



