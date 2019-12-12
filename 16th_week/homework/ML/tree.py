import numpy as np
from collections import Counter
from .metrics import accuracy_score



def gini(y):
    counter = Counter(y)
    result = 0
    for v in counter.values():
        result += (v / len(y)) ** 2
    return 1 - result


def cut(X, y, d, v):
    ind_left = (X[:, d] <= v)
    ind_right = (X[:, d] > v)
    return X[ind_left], X[ind_right], y[ind_left], y[ind_right]


def try_split(X, y):
    best_g = 1
    best_d = -1
    best_v = -1

    for d in range(X.shape[1]):
        sorted_index = np.argsort(X[:, d])
        for i in range(len(X) - 1):

            if X[sorted_index[i], d] == X[sorted_index[i + 1], d]:
                continue

            v = (X[sorted_index[i], d] + X[sorted_index[i + 1], d]) / 2

            X_left, X_right, y_left, y_right = cut(X, y, d, v)
            g_all = gini(y_left) + gini(y_right)

            # print('d={}, v={}, g={}'.format(d, v, g_all))

            if g_all < best_g:
                best_g = g_all
                best_d = d
                best_v = v

    return best_d, best_v, best_g


class DecisionTreeClassifier():

    def __init__(self):
        self.tree_ = None

    def fit(self, X, y):
        self.tree_ = self.create_tree(X, y)
        return self


    def create_tree(self, X, y):
        d, v, g = try_split(X, y)
        if d==-1 or g==0:
            return None

        node = Node(d, v, g)

        X_left, X_right, y_left, y_right = cut(X, y, d, v)

        node.children_left = self.create_tree(X_left, y_left)
        if node.children_left is None:
            lable = Counter(y_left).most_common(1)[0][0]
            node.children_left = Node(l=lable)

        node.children_right = self.create_tree(X_right, y_right)
        if node.children_right is None:
            lable = Counter(y_right).most_common(1)[0][0]
            node.children_right = Node(l=lable)

        return node


    def predict(self, X):

        assert self.tree_ is not None, '请先调用fit()方法训练模型'

        return np.array([self._predict(x, self.tree_) for x in X])


    def _predict(self, x, node):
        """ 返回数据点x在决策树node中的预测类别 """

        if node.label is not None:
            return node.label

        if x[node.dim] <= node.value:
            # left
            return self._predict(x, node.children_left)
        else:
            # right
            return self._predict(x, node.children_right)

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)

        return accuracy_score(y_test, y_predict)


class Node():
    def __init__(self, d=None, v=None, g=None, l=None):
        self.dim = d
        self.value = v
        self.gini = g
        self.label = l

        self.children_left = None
        self.children_right = None

    def __repr__(self):
        return 'Node(d={}, v={}, g={}, l={})'.format(self.dim, self.value, self.gini, self.label)