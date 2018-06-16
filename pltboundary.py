# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 17:21:17 2018

@author: xhj
"""
from pylab import *
from sklearn import datasets

def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
            np.linspace(axis[0], axis[1], int((axis[1]-axis[0])*100)).reshape(-1,1),
            np.linspace(axis[2], axis[3], int((axis[3]-axis[2])*100)).reshape(-1,1)
            )
    X_new = np.c_[x0.ravel(), x1.ravel()]
    
    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)
    
    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap([ '#EF9A9A', '#FFF59D', '#90CAF9' ])
    plt.contourf(x0, x1, zz, linewidth=5, cmap = custom_cmap)
         

# 添加多项式项目  核函数， pipeline
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

def PolynomialLogisticRegression(degree,C=1.0,penalty='l2'):
    return Pipeline([
        ('poly',PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('log_reg', LogisticRegression(C=C, penalty=penalty))
    ])

from sklearn.linear_model import Ridge
def RidgeRegression(degree,alpha=1):
    return Pipeline([
        ('poly',PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('ridge_reg', Ridge(alpha=alpha))
    ])

from sklearn.linear_model import Lasso
def LassoRegression(degree,alpha=1):
    return Pipeline([
        ('poly',PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('lasso_reg', Lasso(alpha=alpha))
    ])


if __name__ == '__main__':
    iris = datasets.load_iris()
    XXX = iris.data[:, 2:]
    yyy = iris.target
    from sklearn.tree import DecisionTreeClassifier

    dt_clf = DecisionTreeClassifier(max_depth=2, criterion = "entropy")
    dt_clf.fit(XXX,yyy)
    plot_decision_boundary(dt_clf, axis= [0.5, 7.5, 0,3])

    plt.scatter(XXX[yyy==0,0], XXX[yyy==0,1])
    plt.scatter(XXX[yyy==1,0], XXX[yyy==1,1])
    plt.scatter(XXX[yyy==2,0], XXX[yyy==2,1])
    plt.show()
                                  