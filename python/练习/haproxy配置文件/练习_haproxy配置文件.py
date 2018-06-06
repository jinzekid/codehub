# Author: Jason Lu

import sys


str_file = "haproxy"
str_file_to_update = "file_to_update"
str_file_to_add = "file_to_add"

f_new = open("haproxy.bak", "w", encoding="utf-8")

is_exist = False
list_retSearch = []

# 提示信息
def func_prompt():
    print("1.search")
    print("2.add")
    print("3.update")
    print("4.delete")
    print("5.quit")

def func_closeFile(f):
    # 判断文件是否关闭
    S1 = f.closed
    if S1:
        print('the file is closed')
    else:
        print('The file donot close')
        f.close()

    return 0

def func_printList(list):
    if list == None:
        print("list is None...")
        return -1

    for v in list:
        print(v)


while is_exist == False:

    # 打开文件
    # f = open(str_file, "r", encoding="utf-8")
    func_prompt()
    input_a = int(input("请输入您的操作:"))

    # 搜索数据
    if input_a == 1:
        list_retSearch.clear()
        str_find = input("请输入关键字:")
        is_searchFind = False
        # 打开文件
        with open(str_file, "r", encoding="utf-8") as f_config:
            # 循环查找字符串
            for line in f_config:
                str_line = line.strip()

                if is_searchFind:
                    print("after search: %s", str_line)
                    if str_line.startswith("server"):
                        list_retSearch.append(str_line)
                        continue
                    else:
                        is_searchFind = False


                if str_find in line and \
                    line.startswith("backend"):
                    is_searchFind = True


            print("\n--------搜索结果--------\n")
            func_printList(list_retSearch)
            print("\n--------end of 搜索结果--------\n")
    elif input_a == 2:
        # 读取新增文件内容
        with open(str_file_to_add, "r", encoding="utf-8") as f_add:
            txt_json = f_add.read()

            list_newRecord = list(eval(txt_json))
            is_searchFind = False

            for v in list_newRecord:
                print(v["backend"])

            # 在原来的配置文件中查找
            with open(str_file, "r", encoding="utf-8") as f_config:

                print("f_config: %s", f_config)
                # 循环查找字符串
                for line in f_config:

                    # 第一步：先把每一行都要写入新文件
                    f_new.write(line)
                    # 第二步：每一行和需要添加的进行比对，如果是就添加新的record
                    str_line = line.strip()
                    for v in list_newRecord:
                        str_find = v["backend"]

                        # 先寻找，如果找到就开始插入数据
                        if str_find in line and \
                                line.startswith("backend"):
                            is_searchFind = True

                        if is_searchFind:
                            for record in v["record"]:
                                str_ret = ""
                                for i in record:
                                    str_ret += str(i) + " " + str(record[i]) + " "

                                print(str_ret)
                                f_new.write("\t\t"+str_ret)
                                f_new.write("\n")

                            is_searchFind = False

                f_new.close()

    elif input_a == 3:
        # 添加数据, 只要追加
        print("更新数据...")

    elif input_a == 4:
        str_data = input("请输入要删除的数据:")

    elif input_a == 5:
        is_exist = True


print("End of Program...Bye!")

func_closeFile(f_new)

