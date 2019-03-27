"""
Created on FEB 28 2019
@author: wangyutian
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

boston = datasets.load_boston()

def skdata2df(skdata):
    dfdata = pd.DataFrame(skdata.data,columns=skdata.feature_names)
    dfdata["target"] = skdata.target
    return dfdata
bs = skdata2df(boston)
print(bs)

boston_X = bs[["RM","LSTAT","PTRATIO"]]

print(boston_X)

boston_y = boston.target

X_train,X_test,y_train,y_test=train_test_split(boston_X,boston_y,test_size=0.3)
linreg = LinearRegression(normalize=True)
linreg.fit(X_train,y_train)
y_pred = linreg.predict(X_test)
print(y_pred)
print(y_test)
print(linreg.coef_)
print(linreg.intercept_)
print(linreg.score(X_test,y_test))

x = np.linspace(1,50,50)
y = x

fig,ax = plt.subplots()
ax.scatter(y_test,y_pred,color="red")
ax.plot(x,y,'k--')
ax.set_xlabel('y_test')
ax.set_ylabel('y_pred')
plt.show()
