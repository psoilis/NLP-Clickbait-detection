import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from utils import confusion_matrix_pretty_print


class RandomForest:

    rdmf = None

    def __init__(self):
        self.rdmf = RandomForestClassifier(n_estimators=500, max_depth=30, bootstrap=False)

    def train(self, training_data, labels):
        self.rdmf = self.rdmf.fit(training_data, labels)

    def predict(self, data, test_labels, plot_conf=False):
        pred_labels = self.rdmf.predict(data)

        print(metrics.confusion_matrix(test_labels, pred_labels))
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

    def hyper_parameter_tuning(self, train_data, train_labels):

        parameters = {'n_estimators': [100, 200, 300, 400, 500, 1000],
                      'max_depth': [20, 30, 40, 50, 60],
                      'min_samples_split': [2, 4, 6],
                      'min_samples_leaf': [1, 2, 4],
                      'bootstrap': [True, False]}

        rdfc = RandomForestClassifier(n_estimators=500, max_depth=30, bootstrap=False)
        clf = GridSearchCV(rdfc, parameters, cv=10)
        print("Starting to fit data")
        clf.fit(train_data, train_labels)

        print("Params: ", clf.best_params_)
        print("Score: ", clf.best_score_)
