#!/usr/bin/python
# -*- coding:utf-8 -*-


USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 BIDUBrowser/7.6 Safari/537.36"

PAGE_SIZE                   =   80  #每页显示几条 20、40、80

STOCK_NO                    =   0   #序号
STOCK_NAME                  =   2   #股票名
STOCK_NEW_PRICE             =   3   #最新价
STOCK_CHANGE_VALUE          =   4   #涨跌额
STOCK_CHANGE_RATIO          =   5   #涨跌百分比
STOCK_BUY                   =   6   #买入
STOCK_SELL                  =   7   #卖出
STOCK_YESTERDAY_CLOSE       =   8   #昨天收盘
STOCK_TODAY_OPEN            =   9   #今天开盘价
STOCK_TODAY_HIGHEST         =   10  #今日最高价
STOCK_TODAY_LOWEST          =   11  #今日最低价
STOCK_TRADE_AMOUNT          =   12  #成交量
STOCK_TRADE_VALUE           =   13  #成交额
STOCK_FINISH_TIME           =   14  #收盘时间
STOCK_AVERAGE_TRADE_AMOUNT  =   15  #平均成交手
STOCK_AVERAGE_TRADE_VALUE   =   16  #平均成交额

LOG_NORMAL      =       2
LOG_WARNING     =       5
LOG_ERROR       =       6
LOG_NORMAL_STR  =       'nor'
LOG_WARNING_STR =       'war'
LOG_ERROR_STR   =       'err'