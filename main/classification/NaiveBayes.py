from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold

import numpy as np

class NaiveBayes:
    gnb = None

    def __init__(self):
        self.gnb = GaussianNB()

    def train(self, training_data, labels):
        self.gnb = self.gnb.fit(training_data, labels)

    def predict(self, data):
        pred_labels = self.gnb.predict(data)
        return pred_labels

    def cross_val(self, data, labels):
        # data = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
        # labels = np.array([1, 2, 2, 1])

        kf = KFold(n_splits=2)
        accuracies = []
        for train_index, test_index in kf.split(data):
            train_set, test_set = data[train_index], data[test_index]
            train_labels, test_labels = labels[train_index], labels[test_index]

            self.train(train_set, train_labels)
            pred = self.gnb.predict_proba(test_set)
            y_pred = self.gnb.predict(test_set)

            accuracy = metrics.accuracy_score(test_labels, y_pred)

            # print(y_pred)
            preds.append(pred)
