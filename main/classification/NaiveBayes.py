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
        # confusion_matrix = metrics.confusion_matrix(test_labels, y_pred, labels=[0, 1, 2])
        return pred_labels

    def cross_validation(self, data, labels):
        kf = KFold(n_splits=10)
        recalls = []
        precisions = []
        accuracies = []
        aucs = []
        for train_index, test_index in kf.split(data):
            train_set, test_set = data[train_index], data[test_index]
            train_labels, test_labels = labels[train_index], labels[test_index]

            self.train(train_set, train_labels)
            y_pred = self.gnb.predict(test_set)

            confusion_matrix = metrics.confusion_matrix(test_labels, y_pred, labels=[0, 1])

            accuracy = metrics.accuracy_score(test_labels, y_pred)
            precision = metrics.precision_score(test_labels, y_pred, labels=[0, 1], average="binary")
            # recall = metrics.recall_score(test_labels, y_pred, labels=[0, 1], average="binary")
            # auc = metrics.roc_auc_score(test_labels, y_pred, average="micro")

            accuracies.append(accuracy)
            precisions.append(precision)
            # recalls.append(recall)
            # aucs.append(auc)

        evaluation = {
            "accuracy": np.mean(accuracies),
            "precision": np.mean(precisions),
            # "recall": np.mean(recalls),
            # "auc": np.mean(aucs)
        }
        return evaluation
