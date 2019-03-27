import tushare as ts
import pymysql
import re

def deleteStockTable():
    # 获取所有股票
    stock_info = ts.get_stock_basics()
    # 连接数据
    conn = pymysql.connect('localhost', 'root', '123456', 'test')
    cursor = conn.cursor()

    codes = stock_info.index
    a = 0
    # 通过for循环以及获取A股只数来遍历每一只股票
    for x in range(0, len(stock_info)):
        # 匹配深圳股票（因为整个A股天多，所以我选择深圳股票做个筛选）
        if re.match('000', codes[x]) or re.match('002', codes[x]):
            # 以stock_加股票代码为表名称创建表格
            cursor.execute('drop table stock_' + codes[x])
            print('%s的表格删除完成' % codes[x])
            a += 1
    print('全部删除共%d张表'%a)
    conn.close()
    cursor.close()


deleteStockTable()