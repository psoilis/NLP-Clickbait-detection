import re
import json_lines
from nltk import ngrams
from utils import utils


def get_ngram_corpus(n):

    ng = {}

    with open('../dataset/instances.jsonl', 'rb') as f:
        for post in json_lines.reader(f):

            grams = ngrams((utils.title(post)[0]).split(), n)

            for g in grams:

                k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()

                if k not in ng.keys():
                    ng[k] = 0

    return ng


def get_ngram_feature_vector(post, n, ngram_word_corpus):

    ngram_feature_vector = ngram_word_corpus

    grams = ngrams((utils.title(post)[0]).split(), n)

    for g in grams:

        k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()

        ngram_feature_vector[k] += 1

    return ngram_feature_vector
