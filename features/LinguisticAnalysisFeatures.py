from utils import utils


# TODO: maybe change that to a module
class LinguisticAnalysisFeatures:
    def __init__(self):
        print("Linguistic Analysis features")

    def get_no_of_characters_features(self, post):
        """
        Calculates the "Number of characters" features. 7 features
        are calculated in total
        :return: a list that contains the features
        """
        f1 = utils.len_characters(utils.title(post))
        f2 = utils.len_characters(utils.ocr(post))
        f3 = utils.len_characters(utils.article(post))
        f4 = utils.len_characters(utils.description(post))
        f5 = utils.len_characters(utils.keywords(post))
        f6 = utils.len_characters(utils.captions(post))
        f7 = utils.len_characters(utils.paragraphs(post))
        return [f1, f2, f3, f4, f5, f6, f7]

    def get_diff_between_no_of_characters_features(self, post):
        """
        Calculates the "Difference between number of chars" features.
        21 features are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_characters(utils.title(post))
        ocr_text_len = utils.len_characters(utils.ocr(post))
        article_title_len = utils.len_characters(utils.article(post))
        article_desc_len = utils.len_characters(utils.description(post))
        article_keywords_len = utils.len_characters(utils.keywords(post))
        article_paragraphs_len = utils.len_characters(utils.paragraphs(post))
        article_captions_len = utils.len_characters(utils.captions(post))

        lst = [post_title_len, ocr_text_len, article_title_len, article_desc_len, article_keywords_len,
               article_paragraphs_len, article_captions_len]

        features_lst = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] != -1 and lst[j] != -1:
                    features_lst.append(abs(lst[i] - lst[j]))
                else:
                    features_lst.append(-1)

        return features_lst

    def get_no_of_characters_ratio_features(self, post):
        print("fix")

    def get_no_of_words_features(self, post):
        """
        Calculates the "Number of words" features. 7 features
        are calculated in total
        :return: a list that contains the features
        """
        f1 = utils.len_words(utils.title(post))
        f2 = utils.len_words(utils.ocr(post))
        f3 = utils.len_words(utils.article(post))
        f4 = utils.len_words(utils.description(post))
        f5 = utils.len_words(utils.keywords(post))
        f6 = utils.len_words(utils.captions(post))
        f7 = utils.len_words(utils.paragraphs(post))
        return [f1, f2, f3, f4, f5, f6, f7]

    def get_diff_between_no_of_words_features(self, post):
        """
        Calculates the "Difference between number of words" features.
        21 features are calculated in total
        :return: a list that contains the features
        """
        post_title_len = utils.len_words(utils.title(post))
        ocr_text_len = utils.len_words(utils.ocr(post))
        article_title_len = utils.len_words(utils.article(post))
        article_desc_len = utils.len_words(utils.description(post))
        article_keywords_len = utils.len_words(utils.keywords(post))
        article_paragraphs_len = utils.len_words(utils.paragraphs(post))
        article_captions_len = utils.len_words(utils.captions(post))

        lst = [post_title_len, ocr_text_len, article_title_len, article_desc_len, article_keywords_len,
               article_paragraphs_len, article_captions_len]

        features_lst = []
        for i in range(len(lst)):
            for j in range(i + 1, len(lst)):
                if lst[i] != -1 and lst[j] != -1:
                    features_lst.append(abs(lst[i] - lst[j]))
                else:
                    features_lst.append(-1)

        return features_lst

    def get_no_of_words_ratio_features(self, post):
        print("fix")

    def get_common_words_features(self, post):
        print("fix")

    def get_no_of_formal_informal_words_features(self, post):
        print("fix")

    def get_formal_informal_words_ratio_features(self, post):
        print("fix")
