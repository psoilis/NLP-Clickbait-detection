import re
import json_lines
from nltk import ngrams
from main.utils import utils

# TODO take only the true clickbait frequencies? ask how this works exactly correct corpus?

def get_ngram_corpus_frequencies(n):

    ng = {}
    count = 0

    with open('../../dataset/corpus.jsonl', 'rb') as f:
        for post in json_lines.reader(f):

            grams = ngrams(utils.article(post).split(), n)

            for g in grams:

                count += 1

                k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()

                print(k)

                if k in ng.keys():
                    ng[k] += 1
                else:
                    ng[k] = 1

        ng = {k: v / count for k, v in ng.items()}

    return ng


def get_ngram_frequency(fname, n):

    ngram_word_freq = {}

    corpus_freqs = get_ngram_corpus_frequencies(n)

    with open(fname, 'rb') as f:
        for post in json_lines.reader(f):

            grams = ngrams(utils.article(post).split(), n)

            f = 0

            for g in grams:

                k = re.sub(r'[^a-zA-Z0-9 ]+', '', (" ".join(g))).lower()

                print(k)

                if k in corpus_freqs:
                    f += corpus_freqs[k]

            ngram_word_freq[utils.post_id(post)] = f

    return ngram_word_freq


# example
print(get_ngram_frequency('../../dataset/instances.jsonl', 2))
