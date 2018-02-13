# Author: Jason Lu
'''
import time
from time import gmtime, strftime

t = time.localtime()
print(time.asctime(t))
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime()))
print(strftime("%A", gmtime()))
print(strftime("%D", gmtime()))
print(strftime("%B", gmtime()))
print(strftime("%y", gmtime()))

# 将秒转换为GMT日期
print(strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(1234567890)))
'''

'''
# 将天数，小时，分钟和秒转换为秒
# 定义常量
SECONDS_PRE_MINUTE  = 60
SECONDS_PRE_HOUR    = 3600
SECONDS_PRE_DAY     = 86400

# 读取来自用户的输入
days = int(input("Enter number of days: "))
hours = int(input("Enter number of Hours: "))
minutes = int(input("Enter number of Minutes: "))
seconds = int(input("Enter number of Seconds: "))

# 计算天数，小时，分钟和秒
total_seconds = days * SECONDS_PRE_DAY
total_seconds += (hours * SECONDS_PRE_HOUR)
total_seconds += (minutes * SECONDS_PRE_MINUTE)
total_seconds += seconds

# 显示结果
print("Total number of seconds: {}".format(total_seconds))
'''

# 利用pandas获取当前日期和时间
import pandas as pd
print(pd.datetime.now())
print(pd.datetime.now().date())
print(pd.datetime.now().year)
print(pd.datetime.now().month)
print(pd.datetime.now().day)
print(pd.datetime.now().hour)
print(pd.datetime.now().minute)
print(pd.datetime.now().second)
print(pd.datetime.now().microsecond)

# 将字符串转换为datetime对象
from datetime import datetime
from dateutil import parser

d1 = "Jan 7 2015 1:15pm"
d2 = "2015 Jan 7 1:33am"

# 知道日期格式
date1 = datetime.strptime(d1, '%b %d %Y %I:%M%p')
print(type(date1))
print(date1)

# 不知道日期格式
date2 = parser.parse(d2)
print(type(date2))
print(date2)


# 毫秒为单位获取当前时间
import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)

# 获取mst，est，utc，gmt和hst形式的当前日期时间
from datetime import datetime
from pytz import timezone

mst = timezone('MST')
print("Time in MST:", datetime.now(mst))
est = timezone('EST')
print("Time in EST:", datetime.now(est))
utc = timezone('UTC')
print("Time in UTC:", datetime.now(utc))
gmt = timezone('GMT')
print("Time in GMT:", datetime.now(gmt))
hst = timezone('HST')
print("Time in HST:", datetime.now(hst))


# 指定日期获取一周中的日期码
d3 = "Jan 7 2016 1:15pm"
date3 = datetime.strptime(d3, '%b %d %Y %I:%M%p')
dayofweek = datetime.date(date3).strftime("%A")
print(dayofweek)
print("weekday():", datetime.date(date3).weekday())
print("isoweekday()", datetime.date(date3).isoweekday())

dayofweek = datetime.today().strftime("%A")
print(dayofweek)
print("weekday():", datetime.today().weekday())
print("isoweekday():", datetime.today().isoweekday())


# 将日期时间对象转化为Unix
import datetime
import time
date_obj = datetime.datetime(2015, 10, 10, 10, 10, 10, 10)
print("Unix Timestamp:", (time.mktime(date_obj.timetuple())))


from dateutil.relativedelta import relativedelta
from datetime import timedelta
import datetime
DATEFORMAT = '%Y-%m-%d %H:%M:%S.%f'

# 时间工具类
class TimeUtil(object):

    # 字符串转日期对象
    @staticmethod
    def stringTodate(strDate, datetimeFormat=DATEFORMAT):
        return datetime.datetime.strptime(strDate, datetimeFormat)

    # 日期对象转字符串
    def dateToString(obj_date, datetimeFormat=DATEFORMAT):
        timestamp = TimeUtil.dateTotimestamp(obj_date=obj_date)
        return TimeUtil.timestampToStrDate(timestamp)

    # 计算两个datatime对象之间的时间差
    @staticmethod
    def betweenWithTwoDates(startDate, endDate, datatimeFormat=DATEFORMAT):
        diff = endDate - startDate
        return diff

    # 将Unix时间戳转换为日期和时间字符串的python程序
    @staticmethod
    def timestampToStrDate(timestamp, datetimeFormat=DATEFORMAT):
        str_date = datetime.datetime.fromtimestamp(timestamp).strftime(datetimeFormat)
        return str_date

    @staticmethod
    def timestampToDate(timestamp, datetimeFormat=DATEFORMAT):
        str_date = datetime.datetime.fromtimestamp(timestamp).strftime(datetimeFormat)
        return TimeUtil.stringTodate(str_date, datetimeFormat)

    # 日期时间对象转化为Unit时间戳
    @staticmethod
    def dateTotimestamp(obj_date):
        return time.mktime(obj_date.timetuple())

    # 添加日
    @staticmethod
    def add_days(days, date=datetime.datetime.today()):
        new_date = date + relativedelta(days=days)
        return new_date

    # 添加月
    @staticmethod
    def add_months(months, date=datetime.datetime.today()):
        new_date = date + relativedelta(months=months)
        return new_date

    # 添加年
    @staticmethod
    def add_years(years, date=datetime.datetime.today()):
        new_date = date + relativedelta(years=years)
        return new_date

    # 添加小时
    @staticmethod
    def add_hours(hours, date=datetime.datetime.today()):
        new_date = date + relativedelta(hours=hours)
        return new_date

    # 添加分
    @staticmethod
    def add_mins(minutes, date=datetime.datetime.today()):
        new_date = date + relativedelta(minutes=minutes)
        return new_date

    # 添加秒
    @staticmethod
    def add_seconds(seconds, date=datetime.datetime.today()):
        new_date = date + relativedelta(seconds=seconds)
        return new_date



print(TimeUtil.add_days(4))
print(TimeUtil.add_months(1))

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


























































































