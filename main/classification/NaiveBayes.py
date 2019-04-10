import numpy as np
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from sklearn.naive_bayes import GaussianNB

from utils import confusion_matrix_pretty_print


class NaiveBayes:
    """
    Class containing the functionality of the MaximumEntropy classifier
    """

    gnb = None

    def __init__(self):
        """
        The class constructor with the optimal hyper-parameters
        """
        self.gnb = GaussianNB(priors=[0.76, 0.24])

    def train(self, training_data, labels):
        """
        Function that trains the classifier

        :arg training_data: Training feature vectors
        :arg labels: Training labels
         """
        self.gnb = self.gnb.fit(training_data, labels)

    def predict(self, data, test_labels, plot_conf=False):
        """
        Function that predicts the labels of test data

        :arg data: The feature vectors that we want to classify
        :arg test_labels: Their original labels for error calculation
        :arg plot_conf: True if we want to plot the confusion matrix

        :returns: the metrics of the prediction process
        """
        pred_labels = self.gnb.predict(data)

        # print(metrics.confusion_matrix(test_labels, pred_labels))
        if plot_conf:
            confusion_matrix_pretty_print.plot_confusion_matrix_from_data(test_labels, pred_labels)

        accuracy = metrics.accuracy_score(test_labels, pred_labels)
        precision = metrics.precision_score(test_labels, pred_labels, labels=[0, 1], average="binary")
        recall = metrics.recall_score(test_labels, pred_labels, labels=[0, 1], average="binary")
        auc = metrics.roc_auc_score(test_labels, pred_labels)
        f1 = metrics.f1_score(test_labels, pred_labels)

        evaluation = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "auc": auc,
            "f1": f1
        }
        return evaluation

    def cross_validation(self, data, labels):
        """
        Function that does stratified k-fold cross validation for better error estimation

        :arg data: The feature vectors that we want to classify
        :arg labels: Their original labels

        :returns: the metrics of the cross validation process
        """
        kf = StratifiedKFold(n_splits=10)
        recalls = []
        precisions = []
        accuracies = []
        aucs = []
        f1s = []
        for train_index, test_index in kf.split(data, labels):
            train_set, test_set = data[train_index], data[test_index]
            train_labels, test_labels = labels[train_index], labels[test_index]

            self.train(train_set, train_labels)
            classif_metrics = self.predict(test_set, test_labels)

            accuracies.append(classif_metrics["accuracy"])
            precisions.append(classif_metrics["precision"])
            recalls.append(classif_metrics["recall"])
            aucs.append(classif_metrics["auc"])
            f1s.append(classif_metrics["f1"])

        evaluation = {
            "accuracy": np.mean(accuracies),
            "precision": np.mean(precisions),
            "recall": np.mean(recalls),
            "auc": np.mean(aucs),
            "f1": np.mean(f1s)
        }
        return evaluation
