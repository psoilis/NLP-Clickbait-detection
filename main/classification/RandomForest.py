import numpy as np
from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import GridSearchCV
from utils import confusion_matrix_pretty_print


class RandomForest:
    """
    Class containing the functionality of the RandomForest classifier
    """

    rdmf = None  # The classifier object

    def __init__(self):
        """
        The class constructor with the optimal hyper-parameters
        """
        self.rdmf = RandomForestClassifier(n_estimators=500, max_depth=30, bootstrap=False)

    def train(self, x_train, y_train):
        """
        Function that trains the classifier

        :arg x_train: Training feature vectors
        :arg y_train: Training labels
         """
        self.rdmf = self.rdmf.fit(x_train, y_train)

    def predict(self, data, test_labels, plot_conf=False):
        """
        Function that predicts the labels of test data

        :arg data: The feature vectors that we want to classify
        :arg test_labels: Their original labels for error calculation
        :arg plot_conf: True if we want to plot the confusion matrix

        :returns: the metrics of the prediction process
        """
        # The predicted labels
        pred_labels = self.rdmf.predict(data)

        # If plot_conf is true then plot the confusion matrix
        if plot_conf:
            confusion_matrix_pretty_print.plot_confusion_matrix_from_data(test_labels, pred_labels)

        # Calculate the accuracy, precision, recall, auc and F1 metrics
        accuracy = metrics.accuracy_score(test_labels, pred_labels)
        precision = metrics.precision_score(test_labels, pred_labels, labels=[0, 1], average="binary")
        recall = metrics.recall_score(test_labels, pred_labels, labels=[0, 1], average="binary")
        auc = metrics.roc_auc_score(test_labels, pred_labels)
        f1 = metrics.f1_score(test_labels, pred_labels)

        # Put the above metrics in a dictionary
        evaluation = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "auc": auc,
            "f1": f1
        }

        # Return the metrics
        return evaluation

    def cross_validation(self, data, labels):
        """
        Function that does stratified k-fold cross validation for better error estimation

        :arg data: The feature vectors that we want to classify
        :arg labels: Their original labels

        :returns: the metrics of the cross validation process
        """
        # Stratified k-fold object
        kf = StratifiedKFold(n_splits=10)
        # Initialize the lists that will contain the metrics
        recalls = []
        precisions = []
        accuracies = []
        aucs = []
        f1s = []

        # Do the training process and put the results in the metric lists
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

        # Put the average of the above metric lists in a dictionary
        evaluation = {
            "accuracy": np.mean(accuracies),
            "precision": np.mean(precisions),
            "recall": np.mean(recalls),
            "auc": np.mean(aucs),
            "f1": np.mean(f1s)
        }

        # Return the metrics
        return evaluation


    def optimize_hyperparams(self, data, labels):
        """
        Function that does the hyper-parameter tuning

        :arg data: The feature vectors that we want to classify
        :arg labels: Their original labels
        """
        # Set of parameters that we want to test and their probable values
        parameters = {'n_estimators': [100, 200, 300, 400, 500, 1000],
                      'max_depth': [20, 30, 40, 50, 60],
                      'min_samples_split': [2, 4, 6],
                      'min_samples_leaf': [1, 2, 4],
                      'bootstrap': [True, False]}

        # Run the hyper-parameter tuning with 10-fold stratified cross-validation
        rdfc = RandomForestClassifier(n_estimators=500, max_depth=30, bootstrap=False)
        clf = GridSearchCV(rdfc, parameters, cv=10)
        clf.fit(data, labels)

        # Print the best hyper-parameters and the score derived from them
        print("Params: ", clf.best_params_)
        print("Score: ", clf.best_score_)
