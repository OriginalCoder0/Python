import numpy as np
from collections import Counter
from .metrics import accuracy_score


class KNeighborClassifier():

    def __init__(self, k=5, p=2):
        assert k > 0, 'k需要大于0'
        assert p > 0, 'p需要大于0'

        self.k = k
        self.p = p

        self._X_train = None
        self._y_train = None

    def fit(self, X_train, y_train):
        assert X_train.shape[0] == y_train.shape[0], 'X_train中样本数量需要与y_train的数量相同'
        assert self.k <= y_train.shape[0], 'k需要小于或等于总的样本数'

        self._X_train = X_train
        self._y_train = y_train


    def predict(self, X_predict):
        '''kNN分类器'''

        assert self._X_train.shape[1] == X_predict.shape[1], '预测的特征数量需要等于样本的特征数量'

        return np.array([self._predict(x) for x in X_predict])

    def _predict(self, x):
        distances = [distance(item, x, p=self.p) for item in self._X_train]
        nearest = np.argsort(distances)[:self.k]
        k_labels = self._y_train[nearest]

        return Counter(k_labels).most_common(1)[0][0]

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)

        return accuracy_score(y_test, y_predict)


def kNN_classify(X_train, y_train, X_predict, k=5, p=2):
    '''kNN分类器'''

    assert k > 0, 'k需要大于0'
    assert k <= y_train.shape[0], 'k需要小于或等于总的样本数'
    assert p > 0, 'p需要大于0'
    assert X_train.shape[0] == y_train.shape[0], 'X_train中样本数量需要与y_train的数量相同'
    assert X_train.shape[1] == X_predict.shape[1], '预测的特征数量需要等于样本的特征数量'

    return np.array([_predict(X_train, y_train, x, k, p) for x in X_predict])


def _predict(X_train, y_train, x, k, p):

    distances = [distance(item, x, p=p) for item in X_train]
    nearest = np.argsort(distances)[:k]
    k_labels = y_train[nearest]

    return Counter(k_labels).most_common(1)[0][0]


def distance(a, b, p=2):
    '''计算距离'''
    return np.sum(np.abs(a - b) ** p) ** (1 / p)
