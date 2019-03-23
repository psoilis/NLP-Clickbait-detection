import json
import json_lines
from features import AbuserDetectionFeatures as adf
from features import ImageFeatures as imf
from features import LinguisticAnalysisFeatures as laf
from utils import utils

image_features = imf.ImageFeatures()
linguistic_features = laf.LinguisticAnalysisFeatures()
abuser_features = adf.AbuserDetectionFeatures()

with open('dataset/instances.jsonl', 'rb') as f:
    for post in json_lines.reader(f):
        print(post)
        print()

        # TODO: call adf, imf, laf methods in order to extract the features
        break  # TODO: remove me


##### TESTS #####
def test_functions():
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
    print("========================================================================")


test_functions()
