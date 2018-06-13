#!/usr/bin/python
# -*- coding:utf-8 -*-
from StockPage import StockPage
from ParseStockPageUtil import *
import math
import time
import gc
import os


# 0:序号 2:股票名 3:最新价 4:涨跌额 5:涨跌百分比 6:买入 7:卖出 8:昨天收盘 9:今天开盘价 10:最高 11:最低 12:成交量(手) 13:成交额(万) 14:收盘时间 15:平均成交手 16:平均成交额

def get_complete_url():
    return url_part_1 + str(url_part_page) + url_part_2 + str(url_part_size) + url_part_3

start = time.time()
name_prefix = get_format_time()



szc_log('%s : steal stock project loading ......' % name_prefix)
szc_log('startup!')
szc_log('start steal stock ...')


url_part_1 = "http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[%22hq%22,%22hs_a%22,%22%22,0,"
url_part_page = 1   #第几页
url_part_2 = ","
url_part_size = Const.PAGE_SIZE     #每页几条
url_part_3 = "]]&callback=FDC_DC.theTableData"

# 记录下第一页，并获得总共几页
page = StockPage(get_complete_url())
name = page.get_date()

# 如果重复则结束
if os.path.exists('./dir_csv/%s_stock.csv' % name):
    szc_log('steal stock repeat!',Const.LOG_WARNING)
    print 'today has stole!'
    exit(0)

page_count = int(math.ceil(page.count / Const.PAGE_SIZE))
arr = page.get_item_arr()
try:
    format_store(arr, name + '_')
    szc_log('steal %s stock : page -> %d ... over!' % (name_prefix, 1), Const.LOG_NORMAL)
except Exception:
    szc_log('steal %s stock error: page -> %d' % (name_prefix, 1), Const.LOG_ERROR)
finally:
    del page

# 记录下剩下页数
for i in range(2,page_count + 1):
    try:
        szc_log('stealing stock info :page -> %d...' % i)
        url_part_page = i
        p = StockPage(get_complete_url())
        a = p.get_item_arr()
        format_store(a, name + '_')
        szc_log('steal stock info :page -> %d ,over!' % i)
        del p
    except Exception:
        szc_log('steal %s stock error: page -> %d' % (name_prefix, i), Const.LOG_ERROR)

gc.collect()
end = time.time()
during_time = end - start
szc_log('steal stock information complete!')
szc_log('total time is %d s' % during_time)
print 'total time is ',during_time
