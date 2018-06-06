#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python 

def func(flt_height, int_count):
    if int_count <= 0:
        return 0

    return (flt_height + 0.6 * flt_height) + func(flt_height * 0.6, int_count -1)


def main():
    
    while True:
        str_continue = input("是否继续程序?(Q或q退出):")
        if str_continue in ['q', 'Q']:
            break

        flt_height = float(input("输入初始高度:"))
        int_count = int(input("输入持续弹跳次数:"))

        total_distance = func(flt_height, int_count)
        print('球运行的总距离:%.2f' %(total_distance))


main()
