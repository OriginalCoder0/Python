import numpy as np

class StandardScaler:

    def __init__(self):
        self.mean_ = None  # 均值
        self.scale_ = None # 标准差

    def fit(self, X):

        self.mean_ = np.mean(X, axis=0)
        self.scale_ = np.std(X, axis=0)

        return self

    def transform(self, X):

        assert self.mean_ is not None and self.scale_ is not None, \
            '请先调用fit方法'

        assert X.shape[1] == len(self.mean_), \
            'X的特征数量需要与fit时传入的数据相同'

        temp = np.empty(shape=X.shape, dtype=float)

        for col in range(X.shape[1]):
            temp[:, col] = (X[:, col] - self.mean_[col]) / self.scale_[col]

        return temp