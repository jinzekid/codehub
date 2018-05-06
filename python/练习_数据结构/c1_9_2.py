#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 

def calu_salary_week():
    salary_hour = float(input("请输入每小时的薪水:"))
    aweek_work_hour = float(input("请输入一周的正常工作时间:"))
    extra_work_hour = float(input("请输入加班时间:"))

    flt_total_salary_aweek = salary_hour * aweek_work_hour + (extra_work_hour * salary_hour * 1.5)

    print("总周薪: %.2f" %(flt_total_salary_aweek))


calu_salary_week()


