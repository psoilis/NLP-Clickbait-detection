import csv
import json_lines
import matplotlib.pyplot as plt
from utils import utils
from pycorenlp import StanfordCoreNLP
from features import AbuserDetectionFeatures as adf
from features import ImageFeatures as imf
from features import LinguisticAnalysisFeatures as laf
from features import SentimentFeatures as sf


def main():
    # Creating label dictionary
    labels = utils.get_label_dict()
    with open('dataset/instances.jsonl', 'rb') as f:
        headers = False
        count = 0  # elements processed
        for post in json_lines.reader(f):
            count += 1
            print('Sample', count)
            # Reading post/article elements
            post_id = utils.post_id(post)
            post_title = utils.title(post)
            article_title = utils.article(post)
            # Extracting sample label
            post_label = labels[post_id]
            # Presence of image in a post
            has_image = imf.image_presence(post)
            # Number of characters
            len_chars_post_title, len_chars_article_title, len_chars_article_desc, len_chars_article_keywords = \
                laf.get_no_of_characters_features(post)
            # Difference between number of characters
            diff_chars_post_title_article_title, diff_chars_post_title_article_desc, diff_chars_post_title_article_keywords, \
            diff_chars_article_title_article_desc, diff_chars_article_title_article_keywords, diff_chars_article_desc_article_keywords = \
                laf.get_diff_between_no_of_characters_features(post)
            # Number of characters ratio
            ratio_chars_post_title_article_title, ratio_chars_post_title_article_desc, ratio_chars_post_title_article_keywords, \
            ratio_chars_article_title_article_desc, ratio_chars_article_title_article_keywords, ratio_chars_article_desc_article_keywords = \
                laf.get_no_of_characters_ratio_features(post)
            # Number of Words
            len_words_post_title, len_words_article_title, len_words_article_desc, len_words_article_keywords = \
                laf.get_no_of_characters_features(post)
            # Difference between number of words
            diff_words_post_title_article_title, diff_words_post_title_article_desc, diff_words_post_title_article_keywords, \
            diff_words_article_title_article_desc, diff_words_article_title_article_keywords, diff_words_article_desc_article_keywords = \
                laf.get_diff_between_no_of_words_features(post)
            # Number of words ratio
            ratio_words_post_title_article_title, ratio_words_post_title_article_desc, ratio_words_post_title_article_keywords, \
            ratio_words_article_title_article_desc, ratio_words_article_title_article_keywords, ratio_words_article_desc_article_keywords = \
                laf.get_no_of_words_ratio_features(post)
            # Post creation hour
            post_creation_hour = adf.get_post_creation_hour(post)
            # Number of sings
            post_title_no_signs = adf.get_no_signs(post_title)
            # Number of hashtags
            post_title_no_hashtags = adf.get_no_hashtags(post_title)
            # Number of exclamations
            post_title_no_exclamations = adf.get_no_exclamations(post_title)
            article_title_no_exclamations = adf.get_no_exclamations(article_title)
            # Number of question marks
            post_title_no_questionmarks = adf.get_no_question_marks(post_title)
            article_title_no_questionmarks = adf.get_no_question_marks(article_title)
            # Number of abbreviations
            post_title_no_abbreviations = adf.get_no_abbreviations(post_title)
            article_title_no_abbreviations = adf.get_no_abbreviations(article_title)
            # Number of ellipses
            post_title_no_ellipses = adf.get_no_ellipses(post_title)
            article_title_no_ellipses = adf.get_no_ellipses(article_title)
            # Number of dots
            post_title_no_dots = adf.get_no_dots(post_title)
            article_title_no_dots = adf.get_no_dots(article_title)
            # Begins with interrogative
            post_title_begins_with_interrogative = adf.get_begins_with_interrogative(post_title)
            article_title_begins_with_interrogative = adf.get_begins_with_interrogative(article_title)
            # Begins with number
            post_title_begins_with_number = adf.get_begins_with_number(post_title)
            article_title_begins_with_number = adf.get_begins_with_number(article_title)
            # Contains determiners and possessives
            post_title_determiners, post_title_possessives = laf.get_det_poses(post_title)
            article_title_determiners, article_title_possessives = laf.get_det_poses(article_title)
            # Contains hyperbolic words
            try:
                nlp = StanfordCoreNLP('http://localhost:9000')
                post_title_hyperbolics, article_title_hyperbolics = sf.get_hyperbolic_words_feature(nlp, post)
            except:
                print("\nServer is not up!")
            # Contains common clickbait phXrases
            post_title_common_phr, article_title_common_phr = laf.get_common_clickbait_phrases_feature(post)
            # # Contains Internet slangs
            post_title_slang, article_title_slang = laf.get_slang_words_feature(post)
            # Sentiment polarity
            post_title_sentiment, article_title_sentiment = sf.get_sentiment_polarity_feature(post)
            # Writing line to file (could write them in batches to improve performance)
            feature_output = post_id + ',' + str(post_label) + ',' + str(has_image) + ',' + str(post_creation_hour) + ',' + str(post_title_begins_with_interrogative) \
                + ',' + str(article_title_begins_with_interrogative) + ',' + str(post_title_begins_with_number) + ',' + str(article_title_begins_with_number) \
                + ',' + str(post_title_determiners) + ',' + str(post_title_possessives) + ',' + str(article_title_determiners) + ',' + str(article_title_possessives) \
                + ',' + str(post_title_hyperbolics) + ',' + str(article_title_hyperbolics) + ',' + str(post_title_common_phr) + ',' + str(article_title_common_phr) \
                + ',' + str(post_title_slang) + ',' + str(article_title_slang) + ',' + str(post_title_sentiment) + ',' + str(article_title_sentiment) \
                + ',' + str(len_chars_post_title) + ',' + str(len_chars_article_title) + ',' + str(len_chars_article_desc) + ',' + str(len_chars_article_keywords) \
                + ',' + str(diff_chars_post_title_article_title) + ',' + str(diff_chars_post_title_article_desc) + ',' + str(diff_chars_post_title_article_keywords) \
                + ',' + str(diff_chars_article_title_article_desc) + ',' + str(diff_chars_article_title_article_keywords) + ',' + str(diff_chars_article_desc_article_keywords) \
                + ',' + str(ratio_chars_post_title_article_title) + ',' + str(ratio_chars_post_title_article_desc) + ',' + str(ratio_chars_post_title_article_keywords) \
                + ',' + str(ratio_chars_article_title_article_desc) + ',' + str(ratio_chars_article_title_article_keywords) + ',' + str(ratio_chars_article_desc_article_keywords) \
                + ',' + str(len_words_post_title) + ',' + str(len_words_article_title) + ',' + str(len_words_article_desc) + ',' + str(len_words_article_keywords) \
                + ',' + str(diff_words_post_title_article_title) + ',' + str(diff_words_post_title_article_desc) + ',' + str(diff_words_post_title_article_keywords) \
                + ',' + str(diff_words_article_title_article_desc) + ',' + str(diff_words_article_title_article_keywords) + ',' + str(diff_words_article_desc_article_keywords) \
                + ',' + str(ratio_words_post_title_article_title) + ',' + str(ratio_words_post_title_article_desc) + ',' + str(ratio_words_post_title_article_keywords) \
                + ',' + str(ratio_words_article_title_article_desc) + ',' + str(ratio_words_article_title_article_keywords) + ',' + str(ratio_words_article_desc_article_keywords) \
                + ',' + str(post_title_no_signs) + ',' + str(post_title_no_hashtags) + ',' + str(post_title_no_exclamations) + ',' + str(article_title_no_exclamations) \
                + ',' + str(post_title_no_questionmarks) + ',' + str(article_title_no_questionmarks) + ',' + str(post_title_no_abbreviations) \
                + ',' + str(article_title_no_abbreviations) + ',' + str(post_title_no_ellipses) + ',' + str(article_title_no_ellipses) + ',' + str(post_title_no_dots) \
                + ',' + str(article_title_no_dots)

            # POS tags extraction
            counts_post_title_POS = laf.get_POS_counts(post_title)
            for key, value in counts_post_title_POS.items():
                feature_output += ',' + str(value)
            counts_article_title_POS = laf.get_POS_counts(article_title)
            for key, value in counts_article_title_POS.items():
                feature_output += ',' + str(value)
            # POS patterns extraction
            post_title_patterns_POS = laf.get_title_patterns(post_title)
            article_title_patterns_POS = laf.get_title_patterns(article_title)
            # Convert True/False to 0/1
            post_title_pattern_nnpv = int(post_title_patterns_POS[0] is True)
            post_title_pattern_nnpt = int(post_title_patterns_POS[1] is True)
            article_title_pattern_nnpv = int(article_title_patterns_POS[0] is True)
            article_title_pattern_nnpt = int(article_title_patterns_POS[1] is True)
            feature_output += ',' + str(post_title_pattern_nnpv) + ',' + str(post_title_pattern_nnpt)
            feature_output += ',' + str(article_title_pattern_nnpv) + ',' + str(article_title_pattern_nnpt)
            # N-gram extraction
            unigrams = laf.get_ngram_counts(post, 1, 6, 1000)
            for key, value in unigrams.items():
                feature_output += ',' + str(value)
            bigrams = laf.get_ngram_counts(post, 2, 6, 200)
            for key, value in bigrams.items():
                feature_output += ',' + str(value)
            trigrams = laf.get_ngram_counts(post, 3, 6, 100)
            for key, value in trigrams.items():
                feature_output += ',' + str(value)
            # If first sample, write the file headers first
            if not headers:
                feature_headers = 'Post_ID,Label,Has_Img,Post_Creation_Hour,Post_Title_Begins_With_Interrogative,' \
                                  'Article_Title_Begins_With_Interrogative,Post_Title_Begins_With_Number,' \
                                  'Article_Title_Begins_With_Number,Post_Title_Contains_Determiners,Post_Title_Contains_Possesives,Article_Title_Contains_Determiners,' \
                                  'Article_Title_Contains_Possesives,Post_Title_Contains_Hyperbolics,Article_Title_Contains_Hyperbolics,Post_Title_Contains_Common_Phrases,' \
                                  'Article_Title_Contains_Common_Phrases,Post_Title_Contains_Slang,Article_Title_Contains_Slang,Post_Title_Sentiment,Article_Title_Sentiment,' \
                                  'Chars_Post_Text,Chars_Article_Title,Chars_Article_Description,Chars_Article_Keywords,' \
                                  'Diff_Char_Post_Title_Article_Title,Diff_Char_Post_Title_Article_Descr,Diff_Char_Post_Title_Article_Keywords,' \
                                  'Diff_Char_Article_Title_Article_Descr,Diff_Char_Article_Title_Article_Keywords,Diff_Char_Article_Descr_Article_Keywords,' \
                                  'Ratio_Char_Post_Title_Article_Title,Ratio_Char_Post_Title_Article_Descr,Ratio_Char_Post_Title_Article_Keywords,' \
                                  'Ratio_Char_Article_Title_Article_Descr,Ratio_Char_Article_Title_Article_Keywords,Ratio_Char_Article_Descr_Article_Keywords,' \
                                  'Words_Post_Text,Words_Article_Title,Words_Article_Description,Words_Article_Keywords,Diff_Words_Post_Title_Article_Title,' \
                                  'Diff_Words_Post_Title_Article_Descr,Diff_Words_Post_Title_Article_Keywords,Diff_Words_Article_Title_Article_Descr,' \
                                  'Diff_Words_Article_Title_Article_Keywords,Diff_Words_Article_Descr_Article_Keywords,Ratio_Words_Post_Title_Article_Title,' \
                                  'Ratio_Words_Post_Title_Article_Descr,Ratio_Words_Post_Title_Article_Keywords,Ratio_Words_Article_Title_Article_Descr,' \
                                  'Ratio_Words_Article_Title_Article_Keywords,Ratio_Words_Article_Descr_Article_Keywords,Post_Title_No_@,Post_Title_No_#,' \
                                  'Post_Title_No_Exclam,Article_Title_No_Exclam,Post_Title_No_Question,Article_Title_No_Question,Post_Title_No_Abbrev,' \
                                  'Article_Title_No_Abbrev,Post_Title_No_Ellipses,Article_Title_No_Ellipses,Post_Title_No_Dots,Article_Title_No_Dots'
                for key, value in counts_post_title_POS.items():
                    feature_headers += ',Post_Title_' + key
                for key, value in counts_article_title_POS.items():
                    feature_headers += ',Article_Title_' + key
                feature_headers += ',Post_Title_NNPV,Post_Title_NNPT'
                feature_headers += ',Article_Title_NNPV,Article_Title_NNPT'
                for key, value in unigrams.items():
                    feature_headers += ',' + key
                for key, value in bigrams.items():
                    feature_headers += ',' + key
                for key, value in trigrams.items():
                    feature_headers += ',' + key
                # Writing file headlines
                with open('dataset/features.csv', encoding='utf8', mode='w',
                          newline='') as features_file:
                    features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    features_writer.writerow([feature_headers])
                headers = True
            with open('dataset/features.csv', encoding='utf8', mode='a', newline='') as features_file:
                features_writer = csv.writer(features_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                features_writer.writerow([feature_output])


def plot_ngram_distribution():
    with open('dataset/NNP/3-gram_frequencies.csv', 'r', encoding='utf8') as csvfile:
        read_csv = csv.reader(csvfile, delimiter=',')
        headers = False
        ngram_counts = []
        for ngram in read_csv:
            if not headers:
                headers = True
                continue
            ngram_counts.append(int(ngram[1]))
        ngram_counts.sort(reverse=True)
        plt.hist(ngram_counts, bins=range(0, 6500, 3))
        plt.yscale('log')
        plt.xscale('log')
        plt.title('Trigram Distribution')
        plt.xlabel('Ngram Count')
        plt.ylabel('Bin Count')
        plt.show()
        plt.clf()


if __name__ == '__main__':
    # plot_ngram_distribution()
    main()

import pandas as pd
from classification import NaiveBayes
from classification import MaximumEntropy

files = [
    # "final_feature_vectors_20.csv",
    # "final_feature_vectors_40.csv",
    # "final_feature_vectors_60.csv",
    # "final_feature_vectors_80.csv",
    # "final_feature_vectors_120.csv",
    "final_feature_vectors_160.csv",
    # "final_feature_vectors_200.csv",
    # "features_no_ngrams.csv",
]

me = MaximumEntropy.MaximumEntropy()
nb = NaiveBayes.NaiveBayes()

for file in files:
    df = pd.read_csv("dataset/" + file)
    X = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values
    y = df['Label'].values

    nb.train(X, y)
    # results = nb.cross_validation(X, y)
    # print(results)

    me.train(X, y)
    # print(svm.cross_validation(X, y))
    # svm.optimize_params(X, y)

    # rf = RandomForest.RandomForest()
    # rf.train(X, y)
    # print(rf.cross_validation(X, y))


df = pd.read_csv("dataset/leftout_test.csv")
X = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values
y = df['Label'].values

print(nb.predict(X, y, True))
print(me.predict(X, y, True))
