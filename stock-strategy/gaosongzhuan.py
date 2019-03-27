import tushare as ts

#基本面数据
basic = ts.get_stock_basics()

#行情和市值数据
hq = ts.get_today_all()
print('成功获取数据')

#当前股价，如果停牌则设置当前价格为上一个加一日股价
hq['trade'] = hq.apply(lambda x:x.settlement if x.trade==0 else x.trade,axis=1)

#分别选取流通股本，总股本，每股公积金，每股收益
basedata = basic[['outstanding','totals','reservedPerShare','esp']]

#选取股票代码，名称，当前价格,总市值，流通市值
hqdata = hq[['code','name','trade','mktcap','nmc']]

#设置行情数据code为index列
hqdata = hqdata.set_index('code')

#合并两个数据表
data = basedata.merge(hqdata,left_index=True,right_index=True)

#将总市值和流通市值换成亿元单位
data['mktcap'] = data['mktcap']/10000
data['nmc'] = data['nmc']/10000

#每股公积金>=5
res = data.reservedPerShare >= 5
#流通股本<=3亿
out = data.outstanding<=30000
#每股收益>=5毛
eps = data.esp >=0.5
#总市值<100亿
mktcap = data.mktcap<=100


allcrit = res & out & eps & mktcap
selected = data[allcrit]

selected[['name','trade','reservedPerShare','outstanding','esp','mktcap','nmc']]
print(len(selected))
print(selected.head(10))
