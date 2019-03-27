import tushare as ts

#获取所有股票列表
data = ts.get_stock_basics()
#print(data.head())

data = data[data.industry=='环境保护']
print(data.head())#返回的环保股数据
print('环保股票数量为',len(data))#计算环保股股票数量


data['code2'] = data.index
#apply方法添加.SZ后缀
data['code2']=
