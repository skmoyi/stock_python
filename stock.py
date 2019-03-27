# import tushare as ts
#
# df = ts.get_realtime_quotes('000581')
#
# df[['code','name','price','bid','ask','volume','amount','time']]
#
# print('1111')

import tushare as ts
df = ts.profit_data(top=60)
df.sort('shares',ascending=False)
