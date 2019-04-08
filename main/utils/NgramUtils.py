import re
import json_lines
import pandas as pd
from nltk import ngrams
from utils import utils


def get_ngram_corpus(n, lower_t, upper_t):

    counts = {}

    with open('dataset/instances.jsonl', 'rb') as f:
        for post in json_lines.reader(f):

            grams = ngrams((utils.article(post)).split(), n)

            for g in grams:

                k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g)))

                if utils.POS_counts(k)['NNP'] == 0:

                    k = k.lower()

                    if k in counts.keys():
                        counts[k] += 1
                    else:
                        counts[k] = 1

    ng = {k: 0 for k, v in counts.items() if v > lower_t and not v >= upper_t}

    pd.DataFrame(counts.items(), columns=['gram', 'count']).to_csv("../dataset/"+n+"-gram_frequencies.csv", index=False)

    return ng


def get_ngram_feature_vector(post, n, ngram_word_corpus: dict):

    ngram_feature_vector = ngram_word_corpus.copy()

    grams = ngrams((utils.article(post)).split(), n)

    for g in grams:

        k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()

        if k in ngram_feature_vector.keys():
            ngram_feature_vector[k] += 1

    return ngram_feature_vector
