import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split


class XGBoost:

    xg_clf = None
    params = None

    def __init__(self, obj, cb, lr, md, a, n, em):
        self.params = {"objective": obj, 'colsample_bytree': cb, 'learning_rate': lr, 'max_depth': md,
                       'alpha': a, 'n_esteimators': n, 'eval_metric': em}
        self. xg_clf  = xgb.XGBClassifier(params=self.params)

    def train(self, x_train, y_train):
        self.xg_clf.fit(x_train, y_train)

    def predict(self, x_test):
        return self.xg_clf.predict(x_test)

    def cross_validation(self, data_dmatrix, metric, folds):
        cv_results = xgb.cv(dtrain=data_dmatrix, params=self.params, nfold=folds,
                            num_boost_round=50, early_stopping_rounds=10, metrics=metric, as_pandas=True, seed=123)
        # metric could be rmse
        cv_results.head()


df = pd.read_csv("../../dataset/features_panos.csv")
X = df.loc[:, ~df.columns.isin(['Label', 'Post_ID'])].values
Y = df['Label'].values

seed = 7
test_size = 0.3
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=test_size, random_state=seed)

xgbc = XGBoost('binary:hinge', 0.5, 0.3, 10, 15, 300, 'error')

xgbc.xg_clf.fit(X_train, y_train)

y_pred = xgbc.xg_clf.predict(X_test)
predictions = [round(value) for value in y_pred]

accuracy = accuracy_score(y_test, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))

cm = confusion_matrix(y_test, predictions)
print(cm)

kfold = KFold(n_splits=10, random_state=7)
results = cross_val_score(xgbc.xg_clf, X, Y, cv=kfold)
print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))
