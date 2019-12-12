import numpy as np

def train_test_split(X, y, test_size=0.25, seed=None):
    """
        将数据集X和y按照test_size设定的比例分割成四份数据：

          X_train 训练数据集
          X_test  测试数据集
          y_train 训练数据集标签
          y_test  测试数据集标签

        并返回这四份数据的元组：
        X_train, X_test, y_train, y_test
    """

    assert X.shape[0] == y.shape[0], "X中样本数量需要等于y中的标签数量"

    assert 0 <= test_size <= 1, "test_size有效范围为0到1之间"

    if seed:
        np.random.seed(seed)

    shuffle = np.random.permutation(len(X))

    size = int(len(X) * test_size)

    test_index = shuffle[:size]
    train_index = shuffle[size:]

    X_train = X[train_index]
    y_train = y[train_index]

    X_test = X[test_index]
    y_test = y[test_index]

    return X_train, X_test, y_train, y_test
