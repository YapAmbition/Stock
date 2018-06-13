#!/usr/bin/python
# -*- coding:utf-8 -*-
import urllib
import urllib2
import Const
import re
import json

class StockPage:
    "每个页面是一个对象"

    def __init__(self, url="http://www.baidu.com"):
        self.url = url
        self.user_agent = Const.USER_AGENT
        self.headers = {'User-Agent': self.user_agent}
        self.values = {}
        self.response = self.get_response(self.url, self.values, self.headers)
        self.content = self.response.read()
        self.json_obj = json.loads(self.get_usage_content())
        self.time = self.json_obj['day']
        self.count = self.json_obj['count']
        self.items = self.json_obj['items']

    def get_date(self):
        return self.time

    def get_usage_content(self):
        partten = re.compile(r'\{.*}',re.IGNORECASE)
        return re.findall(partten, self.content)[0]

    def get_item_arr(self):
        result = []
        for item in self.items:
            result.append(u'序号:%s,股票名:%s,最新价:%s,涨跌额:%s,涨跌百分比:%s,买入:%s,卖出:%s,昨天收盘:%s,今日开盘价:%s,今日最高价:%s,今日最低价:%s,成交量:%s,成交额:%s,收盘时间:%s,平均成交手:%s,平均成交额:%s' % (item[Const.STOCK_NO]
                                                                                                                                                            ,item[Const.STOCK_NAME]
                                                                                                                                                            ,item[Const.STOCK_NEW_PRICE]
                                                                                                                                                            ,item[Const.STOCK_CHANGE_VALUE]
                                                                                                                                                            ,item[Const.STOCK_CHANGE_RATIO]
                                                                                                                                                            ,item[Const.STOCK_BUY]
                                                                                                                                                            ,item[Const.STOCK_SELL]
                                                                                                                                                            ,item[Const.STOCK_YESTERDAY_CLOSE]
                                                                                                                                                            ,item[Const.STOCK_TODAY_OPEN]
                                                                                                                                                            ,item[Const.STOCK_TODAY_HIGHEST]
                                                                                                                                                            ,item[Const.STOCK_TODAY_LOWEST]
                                                                                                                                                            ,item[Const.STOCK_TRADE_AMOUNT]
                                                                                                                                                            ,item[Const.STOCK_TRADE_VALUE]
                                                                                                                                                            ,item[Const.STOCK_FINISH_TIME]
                                                                                                                                                            ,item[Const.STOCK_AVERAGE_TRADE_AMOUNT]
                                                                                                                                                            ,item[Const.STOCK_AVERAGE_TRADE_VALUE]))
        return result


    #   根据 url , values , headers 获得网页响应
    def get_response(self, url, values, headers):
        data = urllib.urlencode(values)
        request = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(request)
        return response

