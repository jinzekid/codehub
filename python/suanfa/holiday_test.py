#!/Users/jasonlu/.virtualenvs/pyvenv37/bin/python

dict_holiday = {"160501": True}

def check_date_isHoliday():

    while True:
        str_date = input("请输入日期(按q或Q退出):")

        if str_date == 'Q' or str_date == 'q':
            break

        if str_date in dict_holiday.keys() and dict_holiday[str_date]:
            print("date:%s is holiday" %str_date)
        else:
            print("date:%s is not holiday" %str_date)

    else:
        print("End Program,,,")


if __name__ == '__main__':
    check_date_isHoliday()

"""
import calendar
cal = calendar.month(2016, 5)
print(cal)

def check_date_isHoliday(s_date):
    str_year  = s_date[:2]
    str_month = s_date[2:4]
    str_day   = s_date[4:]

    if str_day == '01':
        return true

    return False

print(check_date_isHoliday(str_date))
"""







