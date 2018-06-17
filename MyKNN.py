# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 20:19:17 2018

定义一个符合sklearn标准的分类器


@author: xhj
"""
from pylab import *
from math import sqrt
from collections import Counter

class kNNClassifier(object):
    
    def __init__(self, k):
        self.k = k
        self._x_train = None
        self._y_train = None
    
    def fit(self, x_train, y_train):
        # assert
        self._x_train = x_train
        self._y_train = y_train
        return self
    
    def predict（self, x_predict）:
        # assert
        y_predict = [self._predict(x) for x in x_predict]
        return np.array(y_predict)
    

    def _predict(self, x):
        x_train = self._x_train
        y_train = self._y_train
        k = self.k
        assert 1<= k <= x_train.shape[0], 'k must be valid'
        assert x_train.shape[0] == y_train.shape[0], "train's size must be equal to y'size"
        assert x_train.shape[1] == x.shape[0], 'the feature number of x must be right'
        
        distance = np.sqrt(np.sum((X_train-x)**2, axis=1))
        nearest = np.argsort(distance)
        
        topK_y = y_train[nearest[:k]]
        votes = Counter(topK_y)
        
        return votes.most_common(1)[0][0]