import xgboost as xgb


class XGBoost:

    xg_reg = None
    params = None

    def __init__(self, obj, cb, lr, md, a, n):
        self.params = {"objective": obj, 'colsample_bytree': cb, 'learning_rate': lr, 'max_depth': md,
                       'alpha': a, 'n_esteimators': n}
        self. xg_reg = xgb.XGBRegressor(params=self.params)

    def train(self, x_train, y_train):
        self.xg_reg.fit(x_train, y_train)

    def predict(self, x_test):
        return self.xg_reg.predict(x_test)

    def cross_validation(self, data_dmatrix, metric, folds):
        cv_results = xgb.cv(dtrain=data_dmatrix, params=self.params, nfold=folds,
                            num_boost_round=50, early_stopping_rounds=10, metrics=metric, as_pandas=True, seed=123)
        # metric could be rmse
        cv_results.head()


xg = XGBoost('reg:linear', 0.3, 0.1, 5, 10, 10)
xg.cross_validation(_, "rmse", 10)
