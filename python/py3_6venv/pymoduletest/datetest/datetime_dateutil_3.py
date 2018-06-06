# Author: Jason Lu

from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

def main():

    now_time = datetime.now()

    # 输出下一个月最后一天
    last_day_of_next_month = now_time + relativedelta(months=2, day=1, days=-1)

    print(last_day_of_next_month)


if __name__ == '__main__':
    main()


