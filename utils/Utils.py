class Utils:

    def __init__(self):
        print("Utils")

    def img(self, post):
        return "fix"

    def ocr(self, post):
        return "fix"

    def title(self, post):
        # returns the post's title
        return post["postText"]

    def article(self, post):
        # returns the article's title
        return post["targetTitle"]

    def description(self, post):
        # returns the target article's description
        return post["targetDescription"]

    def keywords(self, post):
        # returns the target article's keywords
        return post["targetKeywords"].split(",")

    def paragraphs(self, post):
        # returns the target article's title
        return post["targetParagraphs"]

    def captions(self, post):
        # returns the target article's captions
        return post["targetCaptions"]

    def len_characters(self, content):
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

    def len_words(self, content):
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

    def words(self, content):
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

    def lang_dict_formal(self, content):
        return "fix"

    def lang_dict_informal(self, content):
        return "fix"
