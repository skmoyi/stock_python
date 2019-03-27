import matplotlib.pyplot as plt
# %matplotlib inline
import numpy as np
import pandas as pd
from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_predict
from sklearn.linear_model import LinearRegression
from sklearn import metrics


#read_csv里面的参数时csv在你电脑上的路径，此处csv文件放在notebook运行目录下面的CCPP目录里
data = pd.read_csv('.\CCPP\Folds5x2_pp.csv')
# print(data.head())
# print(data.shape)

# #### 4个参数拟合
# X = data[['AT','V','AP','RH']]
# # print(X.head())
# y = data[['PE']]
# # print(y.head())
# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
# # print(X_train.shape)
# # print(y_train.shape)
# # print(X_test.shape)
# # print(y_test.shape)
# linreg = LinearRegression()
# linreg.fit(X_train,y_train)
# # print(linreg.intercept_)
# # print(linreg.coef_)
# #模型拟合测试集
# y_pred = linreg.predict(X_test)
# #用scikit-learn计算MES
# print("MSE:",metrics.mean_squared_error(y_test,y_pred))
# #用scikit-learn计算RMSE
# print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

# #######三个参数拟合
# X = data[['AT','V','AP']]
# y = data[['PE']]
# X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=1)
# linreg = LinearRegression()
# linreg.fit(X_train,y_train)
# #模型拟合测试集
# y_pred = linreg.predict(X_test)
# #用scikit-learn计算MSE
# print("MSE:",metrics.mean_squared_error(y_test,y_pred))
# #用scikit-learn计算RMSE
# print('RMSE:',np.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#####交叉验证
X = data[['AT','V','AP','RH']]
y = data[['PE']]
linreg = LinearRegression()
predicted = cross_val_predict(linreg,X,y,cv=20)
#用scikit-learn计算MSE
print('MSE:',metrics.mean_squared_error(y,predicted))
#用scikit-learn计算RMSE
print('RMSE',np.sqrt(metrics.mean_squared_error(y,predicted)))

#画图
fig,ax = plt.subplots()
ax.scatter(y,predicted)
ax.plot([y.min(),y.max()],[y.min(),y.max()],'k--',lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
