from sklearn import feature_selection as fs
import numpy as np

T = np.array([
    [1, 0.5, 2, 1],
    [0, 1, 0.1, 0.0],
    [0, 0.1, 1, 0.1],
    [0, 0.1, 0.1, 1]
])
cov = T.dot(T.T)
mean = np.zeros(4)

np.random.seed(0)
Z = np.random.multivariate_normal(mean, cov, size=1000)
X = Z[:, 1:]
y = Z[:, 0]

mi = fs.mutual_info_regression(X, y, random_state=0)
print(mi)
#assert_array_equal(np.argsort(-mi), np.array([1, 2, 0]))

