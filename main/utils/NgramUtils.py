import re
import json_lines
import pandas as pd
from nltk import ngrams
from utils import utils


def get_ngram_corpus(n, lower_t, upper_t):
    """
    Function that initializes the dataset's n-gram feature vectors for given n

    :arg n: The n in n-gram
    :arg lower_t: The lower threshold that removes n-grams with lower counts than the threshold in the dataset
    :arg upper_t: The upper threshold that removes n-grams with higher counts than the threshold  in the dataset

    :return: The final n-gram feature vectors after the upper and lower pruning initialized to zero
    """

    counts = {}  # The dictionary that hold the n-gram occurrences

    # For every post in the dataset
    with open('dataset/instances.jsonl', 'rb') as f:
        for post in json_lines.reader(f):

            grams = ngrams((utils.article(post)).split(), n)  # Get the post's n-grams

            # For every n-gram
            for g in grams:

                k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g)))  # Remove special characters

                # If the n-gram is NNP don't take it into account
                if utils.POS_counts(k)['NNP'] == 0:

                    k = k.lower()  # make i lowercase

                    # Increment the count dictionary
                    if k in counts.keys():
                        counts[k] += 1
                    else:
                        counts[k] = 1

    # Create the final feature vector taking ito account the counts dictionary and the upper and lower thresholds
    ng = {k: 0 for k, v in counts.items() if v > lower_t and not v >= upper_t}

    # Write the results into a csv in order to plot the n-gram distributions afterwards
    pd.DataFrame(counts.items(), columns=['gram', 'count']).to_csv("dataset/"+str(n)+"-gram_frequencies.csv", index=False)

    # Return the final feature vector with 0 values
    return ng


def get_ngram_feature_vector(post, n, ngram_word_corpus: dict):
    """
    Function that creates the n-gram feature vector of a post

    :arg post: The post the we want to extract the n-gram features from
    :arg n: The n in n-gram
    :arg ngram_word_corpus: The entire feature vector initialized with zeroes

    :return: The final n-gram feature vector of the specified post
    """
    # Make a copy of the initialized feature vector to avoid changing it by reference
    ngram_feature_vector = ngram_word_corpus.copy()

    # Find the post's n-grams
    grams = ngrams((utils.article(post)).split(), n)

    # For each n-gram in the post
    for g in grams:

        k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()  # Remove special characters and make it lowercase

        # If it exists in our initialized feature vector add 1
        if k in ngram_feature_vector.keys():
            ngram_feature_vector[k] += 1

    # Return the post's feature vector
    return ngram_feature_vector
