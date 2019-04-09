import xgboost as xgb
from sklearn import metrics
from sklearn.model_selection import StratifiedKFold
from utils import confusion_matrix_pretty_print
import numpy as np
from sklearn.model_selection import GridSearchCV


class XGBoost:

    xg_clf = None
    params = None

    def __init__(self):
        self.params = {"objective: binary:hinge"}
        self. xg_clf = xgb.XGBClassifier(params=self.params)

    def train(self, x_train, y_train):
        self.xg_clf.fit(x_train, y_train)

    def predict(self, data, test_labels, plot_conf=False):

        pred_labels = self.xg_clf.predict(data)

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

        parameters = {'n_estimators': [100, 200, 300],
                      'eta': [0.05, 0.1, 0.2, 0.3],
                      'gamma': [i/10.0 for i in range(0, 5)],
                      'reg_lambda': [1e-5, 1e-2, 0.1, 1, 100],
                      'max_depth': [4, 5, 6],
                      'min_child_weight': [4, 5, 6]
                      }

        c = xgb.XGBClassifier(objective='binary:hinge')
        clf = GridSearchCV(c, cv=10, param_grid=parameters)
        print("Starting to fit data")
        clf.fit(train_data, train_labels)

        print("Params: ", clf.best_params_)
        print("Score: ", clf.best_score_)
