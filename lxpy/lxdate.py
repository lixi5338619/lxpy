# -*- coding: utf-8 -*-
# @Author  : lx

"""
Datetime Library
~~~~~~~~~~~~~~~~~~~~~
"""

import datetime
import time
import re


class DateGo:
    @staticmethod
    def now_data():
        """
        获取当前时间
        :return:  %Y-%m-%d %H:%M:%S
        """
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    @staticmethod
    def now_ymd()->list:
        """
        获取当前 年，月，日
        :return: list:[年,月,日]
        """
        now_date = datetime.datetime.now()
        y = str(now_date.year)
        m = str(now_date.month)
        d = str(now_date.day)
        return [y,m,d]


    @staticmethod                      # 把时间戳 转换为 年月日时分 格式
    def timec_change_dtime(time1):
        if len(str(time1))==13:
            time1 = int(time1) / 1000.0
        timeArray = time.localtime(int(time1))
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
        return otherStyleTime

    
    @staticmethod                      # 负数时间戳转换/转换1970年之前的时间戳
    def netimec_to_dtime(timestamp,valid=True):
        """ 
        :param  timestamp: 负数时间戳
        :param  valid: 默认增加8小时
        :return:  年-月-日 时:分:秒
        if OverflowError , date value out of range: timestamp/1000
        """
        if valid:
            timestamp = int(timestamp) + 8*3600
        result = datetime.datetime(1970, 1, 1) + datetime.timedelta(seconds=int(timestamp))
        return result


    
    @staticmethod
    def dtime_to_timec(tss1):
        """
        把 年月日时分 转换为 时间戳格式
        :param tss1: str
        :return: timeStamp:int
        """
        timeArray = time.strptime(tss1, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(timeArray))
        return timeStamp


    @staticmethod
    def yesterday_timec(day=1):
        """
        # 获取昨天开始的时间戳
        :param day: int
        """
        yesterday = datetime.date.today() - datetime.timedelta(days=day)
        yesterday_timec = int(time.mktime(time.strptime(str(yesterday), '%Y-%m-%d')))
        return yesterday_timec


    @staticmethod
    def difference_time(time1,time2):
        """
        两个时间的差 -> 秒
        """
        t1 = datetime.datetime.utcfromtimestamp(time1)
        t2 = datetime.datetime.utcfromtimestamp(time2)
        time_poor = (t1 - t2).seconds
        return time_poor


    @staticmethod
    def weibo_date(raw):
        """
         # 微博时间处理方法，转换为时间格式
        :param raw: str
        :return:   %Y-%m-%d %H:%M:%S
        """
        result = None
        if raw.find('分钟') != -1 or raw.find('小时') != -1 or raw.find('天') != -1:
            dn = datetime.datetime.now()
            dt = datetime.timedelta
            num = int(re.findall('\d{1,}', raw)[0])
            if '分钟' in raw:
                result = dn - dt(minutes=num)
            elif '小时' in raw:
                result = dn - dt(hours=num)
            elif '天' in raw:
                result = dn - dt(days=num)
            result = result.strftime("%Y-%m-%d %H:%M:%S")
            return result
        elif raw == '刚刚':
            return DateGo.now_data()
        elif len(raw)== 5 and raw[2] == '-':
            result = DateGo.now_ymd()[0] +'-' +raw +' 00:00:00'
            return result
        else:
            if len(raw)==10:
                raw = raw + ' 00:00:00'
                return raw
            else:
                return raw


    @staticmethod
    def youku_date(raw):
        """
        优酷时间处理方法
        """
        if raw == '昨天':
            return DateGo.date_befor_days(1)
        elif raw == '前天':
            return DateGo.date_befor_days(2)
        elif raw == '1周前' or raw=='一周前':
            return DateGo.date_befor_days(7)
        elif raw == '一月前':
            return DateGo.date_befor_days(30)
        elif '天前' in raw:
            return DateGo.youku_date_2(raw)
        elif '刚刚' == raw:
            return DateGo.now_data()
        elif '小时前' in raw:
            return DateGo.youku_date_2(raw)
        elif '分钟前' in raw:
            return DateGo.youku_date_2(raw)


    @staticmethod
    def youku_date_2(raw):
        if raw.find('分钟') != -1 or raw.find('小时') != -1 or raw.find('天') != -1:
            dn = datetime.datetime.now()
            dt = datetime.timedelta
            num = int(re.findall('\d{1,}', raw)[0])
            if  '分钟' in raw:
                result = dn - dt(minutes=num)
            elif '小时' in raw:
                result = dn - dt(hours=num)
            else:
                result = dn - dt(days=num)
            result = result.strftime("%Y-%m-%d %H:%M:%S")
            return result
        else:
            return raw


    @staticmethod
    def difference_timenow(date2):
        """
        当前时间和指定时间的差/-> 秒
        :param date2:
        :return:
        """
        date1 = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        difference = (date1 - date2).total_seconds()
        return difference


    @staticmethod
    def difference_time_two(date1,date2):
        """
        两个时间的差/-> 秒
        :return:
        """
        date1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
        date2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
        difference = (date1 - date2).total_seconds()
        return difference


    @staticmethod
    def date_befor_minutes(value):
        """ 分钟 前/后 的时间
        :param value:
        :return:
        """
        now_time = datetime.datetime.now()
        now_time = now_time - datetime.timedelta(minutes=int(value))
        return now_time.strftime('%Y-%m-%d %H:%M:%S')


    @staticmethod
    def date_befor_hours(value):
        """ 小时前/后 的时间
        :param value:
        :return:
        """
        now_time = datetime.datetime.now()
        now_time = now_time - datetime.timedelta(hours=int(value))
        return now_time.strftime('%Y-%m-%d %H:%M:%S')


    @staticmethod
    def date_befor_days(beforeOfDay:int):
        """ 几天前/后 的时间
        :param beforeOfDay:
        :return:
        """
        today = datetime.datetime.now()
        offset = datetime.timedelta(days=-beforeOfDay)
        re_date = (today + offset).strftime('%Y-%m-%d %H:%M:%S')
        return re_date


    @staticmethod
    def java_date(date,to_format="%Y-%m-%d %H:%M:%S",timezon ="CST"):
        """ java时间格式转换为python日期格式
        %a: 星期的缩写
        %b: 月份英文名的缩写
        %d: 日期(以01-31来表示)
        %Y: 年份(以四位数来表示)
        :param:　data:　Fri May 18 15:46:24 CST 2016
        :param:  timezon：时区 "CST"
        :return: to_format="%Y-%m-%d %H:%M:%S"
        """
        data_format = "%a %b %d %H:%M:%S {} %Y".format(timezon)
        time_struct = time.strptime(str(date),data_format)
        ctime = time.strftime(to_format,time_struct)
        return ctime

