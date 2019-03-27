def test():
    print('1111')


#金叉判定
def jincha(context,bar_dict,his):
    #站上5日线
    def zs5(context,bar_dict,his):
        ma_n = pd.rolling_mean(his,5)
        temp = his - ma_n
        #temp_s包含了前一天站上五日线得股票代码
        temp_s = list(temp[temp>0].iloc[-1,:].dropna().index)
        return temp_s

    #站上10日线
    def zs10(context,bar_dict,his):
        ma_n = pd.rolling_mean(his,10)
        temp = his - ma_n
        temp_s = list(temp[temp>0].iloc[-1,:].dropna().index)
        return temp_s

    #金叉突破
    def jc(context,bar_dict,his):
        mas = pd.rolling_mean(his,5)
        mal = pd.rolling_mean(his,10)
        temp = mas - mal
        #temp_jc昨天大于0股票代码
        #temp_r前天大于0股票代码
        temp_jc = list(temp[temp>0].iloc[-1,:].dropna().index)
        temp_r = list(temp[temp>0].iloc[-2,:].dropna().index)
        temp = []
        for stock in temp_jc:
            if stock not in temp_r:
                temp.append(stock)
        return temp

    #求三种条件下得股票代码交集
    con1 = zs5(context,bar_dict,his)
    con2 = zs10(content,bar_dict,his)
    con3 = jc(context,bar_dict,his)
    tar_list = [con1,con2,con3]
    tarstock = tar_list[0]
    for i in tar_list:
        tarstock = list(set(starstock).intersection(set(i)))

    return tarstock

#过滤次新股、是否停牌、是否涨跌停等条件
def filcon(context,bar_dict,tar_list):
    def zdt_trade(stock,context,bar_dict):
        yesterday = history(2,'1d','close')[stock].values[-1]
        zt = round(1.10*yestoday,2)
        dt = round(0.99*yestoday,2)
        #last最后交易价
        return dt < bar_dict[stock].last < zt
    filstock = []
    for stock in tar_list:
        con1 = ipo_days(stock,context.now) > 60
        con2 = bar_dic[stock].is_trading
        con3 = zdt_trade(stock,context,bar_dict)
        if con1 & con2 & con3:
            filstock.append(stock)
    return filstock

#PCA主成分分析算法
# -*- coding: utf8 -*-
"""
Created on 2019-3-9
PCA source code
@author:wangyutian
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#计算均值，要求输入数据为numpy的矩阵格式，行表示样本数，列表示特征
def meanX(dataX):
    return np.mean(dataX,axis=0)#axis=0表示按照列来求均值，如果输入list,则axis=1

#计算方差，传入的是一个numpy的矩阵格式，行表示样本数，列表示特征
def variance(X):
    m,n = np.shap(X)
    mu = meanX(X)
    muAll = np.tile(mu,(m,1))
    X1 = X - muAll
    variance = 1./m*np.diag(X1.T*X1)
    return variance
#标准化，传入的是一个numpy的矩阵格式，行表示样本数，列表示特征
def normalize(X):
    m,n = np.shape(X)
    mu = meanX(X)
    muAll = np.tile(mu,(m,1))
    X1 = X - muAll
    X2 = np.tile(np.diag(X.T*X),(m,1))
    XNorn = X1/X2
    return XNorn

"""
参数：
    - XMat：传入的是一个numpy的矩阵格式，行表示样本数，列表示特征
    - k:表示取前K个特征值对应的特征向量
返回值：
    - finalData: 参数一指的是返回的低维矩阵，对应于输入参数二
    - reconData: 参数二对应的是移动坐标轴后的矩阵
"""
def pca(XMat,k):
    average = meanX(XMat)
    m,n = np.shape(XMat)
    data_adjust = []
    avgs = np.tile(average,(m,1))
    data_adjust = XMat - avgs
    covX = np.cov(data_adjust.T) #计算协方差矩阵
    featValue,featVec = np.linalg.eig(covX)#求解协方差矩阵的特征值和特征向量
    index = np.argsort(-featValue) #按照featValue进行从大到小排序
    finalData = []
    if k > n:
        print('k must lower than feature number')
        return
    else:
        #注意特征向量时列向量，而numpy的二维矩阵（数组）a[m][n]中，a[1]表示第1行值
        selectVec = np.matrix(featVec.T[index[:k]])#所以这里需要进行转置
        finalData = data_adjust*selectVec.T
        reconData = (finalData * selectVec) + average
    return finalData,reconData

def loaddata(datafile):
    return np.arrat(pd.read_csv(datafile,seo="\t",header=-1)).astype(np.float)

def plotBestFit(data1,data2):
    dataArr1 = np.arrat(data1)
    dataArr2 = np.array(data2)

    m = np.shape(dataArr1)[0]
    axis_x1 = []
    axis_y1 = []
    axis_x2 = []
    axis_y2 = []
    for i in range(m):
        axis_x1.append(dataArr1[i,0])
        axis_y1.append(dataArr1[i,1])
        axis_x2.append(dataArr2[i,0])
        axis_y2.append(dataArr2[i,1])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(axis_x1,axis_y1,s=50,c='red',marker='s')
    ax.scatter(axis_x2,axis_y2,s=50,c='blue')
    plt.xlabel('x1');plt.ylabel('x2')
    plt.savefig("outfile.png")
    plt.show()

#简单测试
#数据来源：http://www.cnblogs.com/jerrylead/archive/2011/04/18/2020209.html
def test():
    X = [[2.5,0.5,2.2,1.9,3.1,2.3,2,1,1.5,1.1],[2.4,0.7,2.9,2.2,3.0,1.6,1.1,1.6,0.9]]
    XMat = np.matrix(X).T
    k = 2
    return pca(XMat,k)
#根据数据集data.txt
def main():
    datafile = "data.txt"
    XMat = loaddata(datafile)
    k = 2
    return pca(XMat,k)

if __name__ = "__main__":
    finalData,reconMat = main()
    plotBestFit(finalData,reconMat)
    
