from sklearn.ensemble import RandomForestClassifier


class RandomForest:

    rdmf = None

    def __init__(self):
        self.rdmf = RandomForestClassifier(n_estimators=100, criterion="entropy", max_depth=10, min_samples_split=2,
                                           min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features="auto",
                                           max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None,
                                           bootstrap=True, oob_score=False, n_jobs=None, random_state=None, verbose=0,
                                           warm_start=False, class_weight=None)

    def train(self, training_data, labels):
        self.rdmf = self.rdmf.fit(training_data, labels)

    def predict(self, data):
        pred_labels = self.rdmf.predict(data)
        return pred_labels

