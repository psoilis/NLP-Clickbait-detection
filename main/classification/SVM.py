from sklearn import svm
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import cross_val_score


class SVM:

    model = None

    def __init__(self):
        self.model = svm.SVC(kernel='linear', gamma='scale')

    def train(self, training_data, labels):
        self.model = self.model.fit(training_data, labels)

    def predict(self, data):
        pred_labels = self.model.predict(data)
        # TODO: calculate AUC, Precision, Recall, Accuracy
        return pred_labels

    def cross_validation(self, data, labels):
        scores = cross_val_score(self.model, data, labels, cv=5)
        accuracy = (scores.mean(), scores.std() * 2)
        print("Accuracy: %0.2f (+/- %0.2f)" % accuracy)
        return accuracy
