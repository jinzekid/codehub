# Author: Jason Lu
from dateutil.relativedelta import relativedelta
from datetime import timedelta, datetime
import datetime, time
DATEFORMAT = '%Y-%m-%d %H:%M:%S.%f'
DATEFORMAT_YMD = '%Y-%m-%d'

# 定义常量
SECONDS_PRE_MINUTE  = 60
SECONDS_PRE_HOUR    = 3600
SECONDS_PRE_DAY     = 86400

# 时间工具类
class timeutil(object):

    # 获取方法的计算时间
    @staticmethod
    def calu_func_time(func):
        start = datetime.now()
        func()
        delta = datetime.now()  - start
        print(func , ":elapsed time in microseconds:" , delta.microseconds)

    # 获取当前时间秒
    @staticmethod
    def get_sec():
        seconds = int(round(time.time()))
        return seconds

    # 获取当前时间的毫秒
    @staticmethod
    def get_millisec():
        milliseconds = int(round(time.time() * 1000))
        return milliseconds

    # 指定的开始日期和结束日期之间获取日期范围
    @staticmethod
    def get_daterange(str_start_date, str_end_date):
        start_date = datetime.datetime.strptime(str_start_date, DATEFORMAT_YMD)
        end_date = datetime.datetime.strptime(str_end_date, DATEFORMAT_YMD)
        end_date = timeutil.addDays(1, end_date)
        date_arr = (start_date + datetime.timedelta(days=x) for x in range(0, (end_date-start_date).days))

        for date_obj in date_arr:
            print(date_obj.strftime(DATEFORMAT_YMD))

    # 获取当前季度的第一天和最后一天
    @staticmethod
    def get_quarter_firstDayAndLastDayWithStrDate(str_date):
        if not str_date:
            return None, None

        date_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        return timeutil.getQuarterFirstDayAndLastDayWithObjDate(date_obj)

    # 获取当前季度的第一天和最后一天
    @staticmethod
    def get_quarter_firstDayAndLastDayWithObjDate(obj_date):
        date_obj = obj_date  # datetime.datetime.strptime(str_date, '%Y-%m-%d')
        current_quarter = round((date_obj.month - 1) / 3 + 1)
        first_date = datetime.datetime(date_obj.year, 3 * current_quarter - 2, 1)
        last_date = datetime.datetime(date_obj.year, 3 * current_quarter + 1, 1) \
                    + timedelta(days=-1)

        return first_date, last_date

    # 获取指定日期的当前月的第一天和最后一天
    @staticmethod
    def get_month_firstDayAndLastDayWithStrDate(str_date):
        if not str_date:
            return None, None

        date_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        return timeutil.getMonthFirstDayAndLastDayWithObjDate(date_obj)


    # 获取指定日期的当前月的第一天和最后一天
    @staticmethod
    def get_month_firstDayAndLastDayWithObjDate(obj_date):
        date_obj = obj_date #datetime.datetime.strptime(str_date, '%Y-%m-%d')
        current_quarter = round((date_obj.month - 1) / 1 + 1)
        first_date = datetime.datetime(date_obj.year, 1 * current_quarter, 1)
        last_date = datetime.datetime(date_obj.year, 1 * current_quarter + 1, 1) \
                    + timedelta(days=-1)

        return first_date, last_date

    # 得到指定日期所在周的开始和结束日期
    @staticmethod
    def get_aweek_startToEndWithStrDate(str_date):
        if not str_date:
            return None, None

        date_obj = datetime.datetime.strptime(str_date, '%Y-%m-%d')
        start_of_week = date_obj - timedelta(days=date_obj.weekday())
        end_of_week = start_of_week + timedelta(days=6)

        return start_of_week, end_of_week

    # 将天数，小时，分钟和秒转换为秒
    @staticmethod
    def calc_sec(days=None, hours=None, minutes=None, seconds=None):
        """
        :param days:
        :param hours:
        :param minutes:
        :param seconds:
        :return:
        """
        total_seconds = 0
        if days:
            total_seconds += days * SECONDS_PRE_DAY
        if hours:
            total_seconds += (hours * SECONDS_PRE_HOUR)
        if minutes:
            total_seconds += (minutes * SECONDS_PRE_MINUTE)
        if seconds:
            total_seconds += seconds
        return total_seconds


    # 根据当前时期找到上一周一和即将到的周一的日期
    @staticmethod
    def find_date(obj_date):
        last_monday = obj_date - datetime.timedelta(days=obj_date.weekday())
        comming_monday = obj_date + datetime.timedelta(days=obj_date.weekday(), weeks=1)
        print(obj_date)
        print(last_monday)
        print(comming_monday)

    # 字符串转日期对象
    @staticmethod
    def format_stringTodate(strDate, datetimeFormat=DATEFORMAT):
        return datetime.datetime.strptime(strDate, datetimeFormat)

    # 日期对象转字符串
    def format_dateToString(obj_date, datetimeFormat=DATEFORMAT):
        timestamp = timeutil.dateTotimestamp(obj_date=obj_date)
        return timeutil.timestampToStrDate(timestamp)

    # 计算两个datatime对象之间的时间差
    @staticmethod
    def calc_interval_twoDates(startDate, endDate, datatimeFormat=DATEFORMAT):
        diff = endDate - startDate
        return diff

    # 将Unix时间戳转换为日期和时间字符串的python程序
    @staticmethod
    def format_timestampToStrDate(timestamp, datetimeFormat=DATEFORMAT):
        str_date = datetime.datetime.fromtimestamp(timestamp).strftime(datetimeFormat)
        return str_date

    @staticmethod
    def foramt_timestampToDate(timestamp, datetimeFormat=DATEFORMAT):
        str_date = datetime.datetime.fromtimestamp(timestamp).strftime(datetimeFormat)
        return timeutil.stringTodate(str_date, datetimeFormat)

    # 日期时间对象转化为Unit时间戳
    @staticmethod
    def format_dateTotimestamp(obj_date):
        return time.mktime(obj_date.timetuple())

    # 添加日
    @staticmethod
    def add_days(days, startDate=datetime.datetime.today()):
        new_date = startDate + relativedelta(days=days)
        return new_date

    # 添加月
    @staticmethod
    def add_months(months, startDate=datetime.datetime.today()):
        new_date = startDate + relativedelta(months=months)
        return new_date

    # 添加年
    @staticmethod
    def add_years(years, startDate=datetime.datetime.today()):
        new_date = startDate + relativedelta(years=years)
        return new_date

    # 添加小时
    @staticmethod
    def add_hours(hours, startDate=datetime.datetime.today()):
        new_date = startDate + relativedelta(hours=hours)
        return new_date

    # 添加分
    @staticmethod
    def add_mins(minutes, startDate=datetime.datetime.today()):
        new_date = startDate + relativedelta(minutes=minutes)
        return new_date

    # 添加秒
    @staticmethod
    def add_sec(seconds, fromDate=datetime.datetime.today()):
        new_date = fromDate + relativedelta(seconds=seconds)
        return new_date

'''
# 测试代码
print()
print(TimeUtil.addDays(4))
print(TimeUtil.addMonths(1))
print(TimeUtil.addYears(1))
print()
str_date = TimeUtil.timestampToStrDate(timestamp=1415419520)
print(str_date)
print()
# 知道日期格式
date1 = datetime.datetime.strptime(str_date, DATEFORMAT)
print(TimeUtil.dateTotimestamp(date1))
print(TimeUtil.stringTodate(strDate=str_date))
print(TimeUtil.dateToString(date1))
print(TimeUtil.timestampToDate(1415419520))
print()

date1 = TimeUtil.stringTodate(strDate='2016-04-16 10:01:27.585')
date2 = TimeUtil.stringTodate(strDate='2016-06-10 09:56:27.067')
diff = TimeUtil.betweenWithTwoDates(startDate=date1, endDate=date2)
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
print()
date1 = TimeUtil.stringTodate(strDate='2016-04-16', datetimeFormat='%Y-%m-%d')
date2 = TimeUtil.stringTodate(strDate='2016-06-10', datetimeFormat='%Y-%m-%d')
diff = TimeUtil.betweenWithTwoDates(startDate=date1, endDate=date2)
print("Difference:", diff)
print("Days:", diff.days)
print("Microseconds:", diff.microseconds)
print("Seconds:", diff.seconds)
print()
print(TimeUtil.addDays(4, startDate=date1))
print()
print(TimeUtil.calculateSeconds(1,0,0,10))
print()
start_of_week, end_of_week = TimeUtil.getWeekStartToEndWithStrDate('2018-02-14')
print(start_of_week, end_of_week)
print()
first_date, end_date = TimeUtil.getMonthFirstDayAndLastDayWithStrDate('2018-05-14')
print(first_date, end_date)
first_date, end_date = TimeUtil.getQuarterFirstDayAndLastDayWithObjDate(datetime.datetime.now())
print(first_date, end_date)
print()
TimeUtil.getDateRange('2016-06-15', '2016-06-18')
'''
