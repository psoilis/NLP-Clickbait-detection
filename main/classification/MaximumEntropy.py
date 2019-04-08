from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression


class MaximumEntropy:

    model = None

    def __init__(self):
        self.model = LogisticRegression(random_state=0,
                                        solver='lbfgs',
                                        multi_class='multinomial')

    def train(self, training_data, labels):
        self.model = self.model.fit(training_data, labels)

    def predict(self, data):
        pred_labels = self.model.predict(data)
        # TODO: calculate AUC, Precision, Recall, Accuracy
        return pred_labels

    def cross_validation(self, data, labels):
        scores = cross_val_score(self.model, data, labels, cv=10)
        accuracy = (scores.mean(), scores.std() * 2)
        print("Accuracy: %0.2f (+/- %0.2f)" % accuracy)
        return accuracy
