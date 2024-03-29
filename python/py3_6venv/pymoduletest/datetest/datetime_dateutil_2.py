# Author: Jason Lu

from datetime import datetime, timedelta

def main():
    # 下个月的最后一个天 = 下下个月的前一天
    now_time = datetime.now()

    if now_time.month in [11, 12]:
        # 获取下下个月第一天的日期对象
        first_day_of_after_two_month = datetime(now_time.year,
                                                now_time.month + 2 - 12,
                                                1)
    else:
        # 获取下下个月第一天的日期对象
        first_day_of_after_two_month = datetime(now_time.year,
                                                now_time.month + 2,
                                                1)

    # 获取下个月最后一天的日期对象
    last_day_of_next_month = first_day_of_after_two_month - timedelta(days=1)

    # 输出结果
    print(last_day_of_next_month.date())


if __name__ == '__main__':
    main()