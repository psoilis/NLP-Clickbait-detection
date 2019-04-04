import json
import json_lines
import csv
from features import AbuserDetectionFeatures as adf
from features import ImageFeatures as imf
from features import LinguisticAnalysisFeatures as laf
from features import SentimentFeatures as sf
from utils import utils
from pycorenlp import StanfordCoreNLP


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
            post_title_no_questionmarks = adf.get_no_questionmarks(post_title)
            article_title_no_questionmarks = adf.get_no_questionmarks(article_title)
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
            post_title_determiners, post_title_possessives = laf.get_det_poses(post, 'title')
            # Contains hyperbolic words
            try:
                nlp = StanfordCoreNLP('http://localhost:9000')
                post_title_hyperbolics = sf.get_hyperbolic_words_feature(nlp, post)
            except:
                print("\nServer is not up!")
            # Sentiment polarity
            post_title_sentiment = sf.get_sentiment_polarity_feature(post)
            # Contains common clickbait phrases
            post_title_common_phr = laf.get_common_clickbait_phrases_feature(post)  # everything zero
            # Contains Internet slangs
            post_title_slang = laf.get_slang_words_feature(post)  # have to make it exact match and not in work
            # Writing line to file (could write them in batches to improve performance)
            feature_output = post_id + ',' + str(post_label) + ',' + str(has_image) + ',' + str(post_creation_hour) + ',' + str(post_title_begins_with_interrogative)\
                + ',' + str(article_title_begins_with_interrogative) + ',' + str(post_title_begins_with_number) + ',' + str(article_title_begins_with_number)  \
                + ',' + str(post_title_determiners) + ',' + str(post_title_possessives) + ',' + str(post_title_hyperbolics) + ',' + str(post_title_common_phr) \
                + ',' + str(post_title_slang) + ',' + str(post_title_sentiment) + ',' + str(len_chars_post_title) + ',' + str(len_chars_article_title) \
                + ',' + str(len_chars_article_desc) + ',' + str(len_chars_article_keywords) + ',' + str(diff_chars_post_title_article_title) \
                + ',' + str(diff_chars_post_title_article_desc) + ',' + str(diff_chars_post_title_article_keywords) + ',' + str(diff_chars_article_title_article_desc)\
                + ',' + str(diff_chars_article_title_article_keywords) + ',' + str(diff_chars_article_desc_article_keywords) + ',' + str(ratio_chars_post_title_article_title)\
                + ',' + str(ratio_chars_post_title_article_desc) + ',' + str(ratio_chars_post_title_article_keywords) + ',' + str(ratio_chars_article_title_article_desc)\
                + ',' + str(ratio_chars_article_title_article_keywords) + ',' + str(ratio_chars_article_desc_article_keywords) + ',' + str(len_words_post_title)\
                + ',' + str(len_words_article_title) + ',' + str(len_words_article_desc) + ',' + str(len_words_article_keywords) + ',' + str(diff_words_post_title_article_title)\
                + ',' + str(diff_words_post_title_article_desc) + ',' + str(diff_words_post_title_article_keywords) + ',' + str(diff_words_article_title_article_desc)\
                + ',' + str(diff_words_article_title_article_keywords) + ',' + str(diff_words_article_desc_article_keywords) + ',' + str(ratio_words_post_title_article_title)\
                + ',' + str(ratio_words_post_title_article_desc) + ',' + str(ratio_words_post_title_article_keywords) + ',' + str(ratio_words_article_title_article_desc)\
                + ',' + str(ratio_words_article_title_article_keywords) + ',' + str(ratio_words_article_desc_article_keywords) + ',' + str(post_title_no_signs)\
                + ',' + str(post_title_no_hashtags) + ',' + str(post_title_no_exclamations) + ',' + str(article_title_no_exclamations) + ',' + str(post_title_no_questionmarks)\
                + ',' + str(article_title_no_questionmarks) + ',' + str(post_title_no_abbreviations) + ',' + str(article_title_no_abbreviations) + ',' + str(post_title_no_ellipses)\
                + ',' + str(article_title_no_ellipses) + ',' + str(post_title_no_dots) + ',' + str(article_title_no_dots)
            # POS tags extraction
            counts_POS = laf.get_POS_counts(post)
            for key, value in counts_POS.items():
                feature_output += ',' + str(value)
            # POS patterns extraction
            patterns_POS = laf.get_title_patterns(post)
            # Convert True/False to 0/1
            pattern_nnpv = int(patterns_POS[0] is True)
            pattern_nnpt = int(patterns_POS[1] is True)
            feature_output += ',' + str(pattern_nnpv) + ',' + str(pattern_nnpt)
            # N-gram extraction
            unigrams = laf.get_ngram_counts(post, 1, 3)
            for key, value in unigrams.items():
                feature_output += ',' + str(value)
            bigrams = laf.get_ngram_counts(post, 2, 3)
            for key, value in bigrams.items():
                feature_output += ',' + str(value)
            trigrams = laf.get_ngram_counts(post, 3, 3)
            for key, value in trigrams.items():
                feature_output += ',' + str(value)
            # If first sample, write the file headers first
            if not headers:
                feature_headers = 'Post_ID,Label,Has_Img,Post_Creation_Hour,Post_Title_Begins_With_Interrogative,' \
                                  'Article_Title_Begins_With_Interrogative,Post_Title_Begins_With_Number,' \
                                  'Article_Title_Begins_With_Number,Post_Title_Contains_Determiners,Post_Title_Contains_Possesives,' \
                                  'Post_Title_Contains_Hyperbolics,Post_Title_Contains_Common_Phrases,Post_Title_Contains_Slang,' \
                                  'Post_Title_Sentiment,Chars_Post_Text,Chars_Article_Title,Chars_Article_Description,Chars_Article_Keywords,' \
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
                for key, value in counts_POS.items():
                    feature_headers += ',' + key
                feature_headers += ',NNPV,NNPT'
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

##### TESTS #####
def test_functions(post):
    post = '{"id":"608310377143799810",' \
           '"postTimestamp":"Tue Jun 09 16:31:10 +0000 2015",' \
           '"postText":["Apple\'s iOS 9 \'App thinning\' feature will give your phone\'s storage a boost"],' \
           '"postMedia":[],' \
           '"targetTitle":"Apple gives back gigabytes: iOS 9 \'app thinning\' feature will finally give your phone\'s storage a boost",' \
           '"targetDescription":"\'App thinning\' will be supported on Apple\'s iOS 9 and later models. It ensures apps use the lowest amount of storage space by \'slicing\' it to work on individual handsets (illustrated).","targetKeywords":"Apple,gives,gigabytes,iOS,9,app,thinning,feature,finally,phone,s,storage,boost","targetParagraphs":["Paying for a 64GB phone only to discover that this is significantly reduced by system files and bloatware is the bane of many smartphone owner\'s lives. ","And the issue became so serious earlier this year that some Apple users even sued the company over it. ","But with the launch of iOS 9, Apple is hoping to address storage concerns by introducing a feature known as \'app thinning.\'","It has been explained on the watchOS Developer Library site and is aimed at developers looking to optimise their apps to work on iOS and the watchOS. ","It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs run on the particular handset it is being installed onto.","It \'slices\' the app into \'app variants\' that only need to access the specific files on that specific handset. ","XperiaBlog recently spotted that the 8GB version of Sony\'s mid-range M4 Aqua has just 1.26GB of space for users. ","This means that firmware, pre-installed apps and Android software take up a staggering 84.25 per cent. ","Sony does let users increase storage space using a microSD card, but as XperiaBlog explained: \'Sony should never have launched an 8GB version of the Xperia M4 Aqua. ","\'If you are thinking about purchasing this model, be aware of what you are buying into.\'","Previously, apps would need to be able to run on all handsets and account for the varying files, chipsets and power so contained sections that weren\'t always relevant to the phone it was being installed on.","This made them larger than they needed to be. ","Under the new plans, when a phone is downloaded from the App Store, the app recognises which phone it is being installed onto and only pulls in the files and code it needs to work on that particular device. ","For iOS, sliced apps are supported on the latest iTunes and on devices running iOS 9.0 and later. ","In all other cases, the App Store will deliver the previous \'universal apps\' to customers.","The guidelines also discuss so-called \'on-demand resources.\' This allows developers to omit features from an app until they are opened or requested by the user. ","The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. ","This will also increase how quickly an app downloads. ","An example given by Apple is a game app that may divide resources into game levels and request the next level of resources only when the app anticipates the user has completed the previous level.","Similarly, the app can request In-App Purchase resources only when the user buys a corresponding in-app purchase.","Apple explained the operating system will then \'purge on-demand resources when they are no longer needed and disk space is low\', removing them until they are needed again.","And the whole iOS 9 software has been designed to be thinner during updates, namely from 4.6GB to 1.3GB, to free up space. ","This app thinning applies to third-party apps created by developers. ","Apple doesn\'t say if it will apply to the apps Apple pre-installed on devices, such as Stocks, Weather and Safari - but it is likely that it will in order to make iOS 9 smaller. ","As an example of storage space on Apple devices, a 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. ","A drop of 8GB, leaving 87.5 per cent of storage free. ","By comparison, Samsung\'s 64GB S6 Edge has 53.42GB of available space, and of this 9GB is listed as system memory. ","Although this is a total drop of almost 11GB, it equates to 83 per cent of space free. ","By comparison, on a 32GB S6 MailOnline found 23.86GB of space was available, with 6.62GB attributed to system memory.","This is a drop of just over 8GB and leaves 75 per cent free.","Samsung said it, too, had addressed complaints about bloatware and storage space with its S6 range.  ","Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54 per cent and 79 per cent of free space."," ","Businessman \'killed his best friend when he crashed jet-powered dinghy into his £1million yacht while showing off\' as his wife filmed them"],"targetCaptions":["\'App thinning\' will be supported on Apple\'s iOS 9 and later models. It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs to run on individual handsets. It \'slices\' the app into \'app variants\' that only need to access the specific files on that specific device","\'App thinning\' will be supported on Apple\'s iOS 9 and later models. It ensures apps use the lowest amount of storage space on a device by only downloading the parts it needs to run on individual handsets. It \'slices\' the app into \'app variants\' that only need to access the specific files on that specific device","The guidelines also discuss so-called \'on-demand resources.\' This allows developers to omit features from an app until they are opened or requested by the user. The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. This will also increase how quickly an app downloads","The guidelines also discuss so-called \'on-demand resources.\' This allows developers to omit features from an app until they are opened or requested by the user. The App Store hosts these resources on Apple servers and manages the downloads for the developer and user. This will also increase how quickly an app downloads","Apple said it will then \'purge on-demand resources when they are no longer needed and disk space is low\' (Apple\'s storage menu is pictured)","Apple said it will then \'purge on-demand resources when they are no longer needed and disk space is low\' (Apple\'s storage menu is pictured)","A 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. A drop of 8GB, leaving 87.5 % of storage free. Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54% and 79% of free space (illustrated)","A 64GB Apple iPhone 6 is typically left with 56GB of free space after pre-installed apps, system files and software is included. A drop of 8GB, leaving 87.5 % of storage free. Previous handsets, including the Samsung Galaxy S4 and Apple iPhone 5C typically ranged from between 54% and 79% of free space (illustrated)","Earlier this year, a pair of disgruntled Apple users filed a lawsuit in Miami accusing the tech giant of \'concealing, omitting and failing to disclose\' that on 16GB versions of iPhones, more than 20% of the advertised space isn\'t available. This graph reveals the capacity available and unavailable to the user","Earlier this year, a pair of disgruntled Apple users filed a lawsuit in Miami accusing the tech giant of \'concealing, omitting and failing to disclose\' that on 16GB versions of iPhones, more than 20% of the advertised space isn\'t available. This graph reveals the capacity available and unavailable to the user"]}'
    post = json.loads(post)

    print("========================================================================")
    post_title = utils.title(post)
    print("Post title: ", post_title)
    article_title = utils.article(post)
    print("Article title: ", article_title)
    article_desc = utils.description(post)
    print("Article description: ", article_desc)
    article_keywords = utils.keywords(post)
    print("Article keywords: ", article_keywords)
    article_paragraphs = utils.paragraphs(post)
    print("Article paragraphs: ", article_paragraphs)
    article_captions = utils.captions(post)
    print("Article captions: ", article_captions)

    # characters length test
    len_chars = utils.len_characters("")
    print("Chars length = ", len_chars)
    len_chars = utils.len_characters("1341 4314 hehehe")
    print("Chars length = ", len_chars)
    len_chars = utils.len_characters(["123", "12345"])
    print("Chars length = ", len_chars)

    # words length test
    len_words = utils.len_words("")
    print("Words length = ", len_words)
    len_words = utils.len_words("1341 4314 hehehe")
    print("Words length = ", len_words)
    len_words = utils.len_words(["I am", "You are a prick", "yolo"])
    print("Words length = ", len_words)

    # words test
    words = utils.words("")  # TODO: Should we return -1 in that case???
    print("Words = ", words)
    words = utils.words("1341 4314 hehehe")
    print("Words = ", words)
    words = utils.words(["I am", "You are a prick", "yolo"])
    print("Words = ", words)

    # get_no_of_characters_features tests
    test_dict = {
        "postText": "Check dis car",   # chars 13, words 3
        "postMedia": "",
        "targetTitle": "Mustang",   # chars 7, words 1
        "targetDescription": "Mustang GT",  # chars 10, words 2
        "targetKeywords": "keyword1,keyword2",  # average 8, words 1
        "targetCaptions": ["Caption len 14", "Length 8"],  # average 11, words 2.5
        "targetParagraphs": ["This is a paragraph with length 34", "Another with length 22"]   # average 28, words 5.5
    }
    test_dict_empty = {
        "postText": "",
        "postMedia": "",
        "targetTitle": "",
        "targetDescription": "",
        "targetKeywords": "",
        "targetCaptions": [],
        "targetParagraphs": []
    }
    features = laf.get_no_of_characters_features(test_dict)
    print("No of chars features: ", features)
    features = laf.get_no_of_characters_features(test_dict_empty)
    print("No of chars features (empty): ", features)
    features = laf.get_no_of_words_features(test_dict)
    print("No of words features: ", features)
    features = laf.get_no_of_words_features(test_dict_empty)
    print("No of words features (empty): ", features)
    features = laf.get_diff_between_no_of_words_features(test_dict)
    print("Diff of no of words features: ", features)
    features = laf.get_diff_between_no_of_words_features(test_dict_empty)
    print("Diff of no of words features: (empty) ", features)
    print("========================================================================")
	
	# print(post)
    # Activity Based Characteristics
    post_title = utils.title(post)
    print("Post title: ", post_title)
    post_title_signs = adf.get_no_signs(post_title)
    print("Post title @ Signs: ", post_title_signs)
    post_title_hashtags = adf.get_no_hashtags(post_title)
    print("Post title # Hashtags: ", post_title_hashtags)
    # post_title_punctuation = adf.get_no_punctuation(post_title)
    # print("Post title Punctuation: ", post_title_punctuation)
    article_paragraphs = utils.paragraphs(post)
    print("Article paragraphs: ", article_paragraphs)
    article_paragraphs_signs = adf.get_no_signs(article_paragraphs)
    print("Article paragraphs @ Signs: ", article_paragraphs_signs)
    article_paragraphs_hashtags = adf.get_no_hashtags(article_paragraphs)
    print("Article paragraphs # Hashtags: ", article_paragraphs_hashtags)
    # article_paragraphs_punctuation = adf.get_no_punctuation(post_title)
    # print("Article paragraphs Punctuation: ", article_paragraphs_punctuation)
    # Article Properties
    article_keywords = utils.keywords(post)
    print("Article Keywords: ", article_keywords)
    article_paragraphs = utils.paragraphs(post)
    print("Article paragraphs: ", article_paragraphs)
    article_captions = utils.captions(post)
    print("Article captions: ", article_captions)
    ## Post Longevity
    # post_timestamp = datetime.strptime(utils.timestamp(post), '%a %b %d %H:%M:%S %z %Y')
    # print("Post timestamp: ", post_timestamp)
    # post_longevity = adf.get_post_longevity(post_timestamp)
    # print("Post longevity in minutes: ", post_longevity)
    # post_creation_slot = adf.get_post_creation_hour(post_timestamp)
    # print("Post Creation slot: ", post_creation_slot)

    # common phrases test
    test_dict = {
        "postText": "Check dis car",
    }
    test_dict_clicbait = {
        "postText": "Can't Even Handle this workout!",
    }
    clickbait_feat = laf.get_common_clickbait_phrases_feature(test_dict)
    print("Clickbait phrase: ", clickbait_feat)
    clickbait_feat = laf.get_common_clickbait_phrases_feature(test_dict_clicbait)
    print("Clickbait phrase: ", clickbait_feat)

    # slang abbreviations test
    test_dict = {"postText": "tyri kai psomi"}  # "ty" exists but not as an exact match
    test_dict_slang = {"postText": "Ty for helping me"}

    slang_feat = laf.get_slang_words_feature(test_dict)
    print("Slang feat: ", slang_feat)
    slang_feat = laf.get_slang_words_feature(test_dict_slang)
    print("Slang feat: ", slang_feat)
    # hyperbolic words
    try:
        test_dict = {"postText": "What Are The Best Things To Do In Charleston, South Carolina?"}   # best
        test_dict_nonh = {"postText": "a random non hyperbolic sentence"}
        nlp = StanfordCoreNLP('http://localhost:9000')
        hfeat = sf.get_hyperbolic_words_feature(nlp, test_dict)
        print("Hyperbolic Words Feature: ", hfeat)
        hfeat = sf.get_hyperbolic_words_feature(nlp, test_dict_nonh)
        print("Hyperbolic Words Feature: ", hfeat)
    except:
        print("\nServer is not up!")
    # sentiment polarity
    test_dict_bad = {"postText": "Check how he died in reality"}
    test_dict_good = {"postText": "Learn this amazing technique"}
    pol_feat = sf.get_sentiment_polarity_feature(test_dict_bad)
    print("Polarity Feature: ", pol_feat)
    pol_feat = sf.get_sentiment_polarity_feature(test_dict_good)
    print("Polarity Feature: ", pol_feat)


if __name__ == '__main__':
    main()
