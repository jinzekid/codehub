#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python

def read_salary():

    while True:
        str_file_name = input("请输入雇员列表文件名(q或Q退出):")
        
        if str_file_name is None or str_file_name == '':
           continue  
        
        if str_file_name in ['q', 'Q']:
           break 
        
        list_employ = []
        try:
            with open(str_file_name, 'r', encoding='utf-8') as f:
                for one_employ in f:
                    employ = one_employ.strip()
                    if employ != '':
                        list_employ.append(employ)

        except FileNotFoundError as e:
            print('没有对应的文件...请重新输入文件名')

        if len(list_employ) <= 0:
            print('暂时没有员工信息!')

        print(len(list_employ))
        print('\n')
        print('------------------员工支付工资信息表------------------')
        for employ in list_employ:
            print(employ)
        print('-----------------------------------------------------')


read_salary()
