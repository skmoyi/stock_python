import tushare as ts

df = ts.get_hist_data('000627', '2019-01-01', '2019-02-28')

for i in range(0,len(df)):
    try:
        print(i)
    except:
        print('错误')