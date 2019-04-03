import numpy as np
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold


class NaiveBayes:
    gnb = None

    def __init__(self):
        self.gnb = GaussianNB()

    def train(self, training_data, labels):
        self.gnb = self.gnb.fit(training_data, labels)

    def predict(self, data):
        pred_labels = self.gnb.predict(data)
        # TODO: calculate AUC, Precision, Recall, Accuracy
        return pred_labels

    def cross_validation(self, data, labels):
        kf = KFold(n_splits=10)
        accuracies = []
        for train_index, test_index in kf.split(data):
            train_set, test_set = data[train_index], data[test_index]
            train_labels, test_labels = labels[train_index], labels[test_index]

            self.train(train_set, train_labels)
            y_pred = self.gnb.predict(test_set)

            accuracy = metrics.accuracy_score(test_labels, y_pred)
            # confusion_matrix = metrics.confusion_matrix(test_labels, y_pred, labels=[0, 1, 2])
            accuracies.append(accuracy)

        accuracies_average = np.mean(accuracies)
        return accuracies_average
