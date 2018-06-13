#!/usr/bin/python
# -*- coding:utf-8 -*-

import time
import Const

def print_obj(obj):
    print '\n'.join(['%s:%s' % item for item in obj.__dict__.items()])

def format_store(array, prefix = ''):
    # 为了bat  我妥协了写绝对路径
    # 不  我绝不妥协
    f_csv = open('./dir_csv/' + prefix + 'stock.csv', 'a')
    for item in array:

        tmp_arr = item.split(',')
        for value in tmp_arr:
            f_csv.write(value.split(':')[1].encode('utf-8'))
            f_csv.write(',')
        f_csv.write('\n')
    f_csv.close()

def get_format_time(f = '%Y%m%d', t = None):
    return time.strftime(f, time.localtime(t or time.time()))

def szc_log(ss, level = 2):
    level_str = Const.LOG_NORMAL_STR
    if level == Const.LOG_NORMAL:
        level_str = Const.LOG_NORMAL_STR
    elif level == Const.LOG_WARNING:
        level_str = Const.LOG_WARNING_STR
    else:
        level_str = Const.LOG_ERROR_STR
    f_name = './logs/log_' + level_str + '_' + get_format_time(f = '%Y%m%d%H') + '.log'
    f = open(f_name,'a')
    f.write(ss)
    f.write('\n')
    f.close()
