# Author: Jason Lu
from datetime import datetime
from dateutil.rrule import rrule, DAILY, MO, WE

def main():
    rrule_obj = rrule(DAILY, #每天
                      byweekday=(MO, WE), #周一，周三
                      dtstart=datetime(2012, 1, 1), #2012.1.1日起
                      until=datetime(2012, 2, 1))#2012.2.1日止

    # 逐个取出符合条件的日期对象
    for dt in rrule_obj:
        print(dt)

if __name__ == '__main__':
    main()