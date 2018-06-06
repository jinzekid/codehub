#! /Users/jasonlu/.virtualenvs/pyven3_6/bin/python
import os

#-------------------------------------------------------#
"""
是否退出
"""
def b_quit(str):
    if str in ['q', 'Q']:
        return True
    return False

"""
列出所有文件
"""
def show_all_files():
    str_work_path = os.getcwd()
    list_files = os.listdir(str_work_path)
    list_sort_file_name = sorted(list_files)
    print('>>>当前文件列表<<<')
    for str_file in list_sort_file_name:
        print(str_file)
    print('>>>------------<<<')

#-------------------------------------------------------#
def main():

    while True:
        # 显示当前目录中所有文件
        show_all_files()
        # 询问用户创建文本
        str_file_name = input('请输入要创建的文件名称(q或Q退出):')

        if str_file_name == '':
            print('文件名不能为空...')
            continue

        if b_quit(str_file_name): 
            print('Bye...')
            break

        str_confirm = input('是否确定?(确定(y or Y), 取消(n or N)')

        b_continue_input_file_content = False
        if str_confirm in ['y', 'Y']:
            b_continue_input_file_content = True

        # 输入文本内容
        f = open(str_file_name, 'w', encoding='utf-8')
        while b_continue_input_file_content:
            str_content = input('请输入内容(q或Q退出):')
            if b_quit(str_content):
                break
            f.write(str_content)
            f.write('\n')
            print('写入完成...继续...')

        f.close()
        print('>>>' + str_file_name +"文件保存成功<<< ")


#-------------------------------------------------------#
if __name__ == '__main__':
    main()

