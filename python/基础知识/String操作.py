# Author: Jason Lu
"""
字符串工具，封装常用字符串功能
"""
class str_util(object):

    """
    分割为子字符串组成的列表
    """
    @staticmethod
    def split(str_org, str_split=""):
        if str_split == "":
            return str_org.split()

        return str_org.split(str_split)


    """
    字符串连接
    """
    @staticmethod
    def join(list_str, str_join):

        return str_join.join(list_str)


    """
    字符串截取
    """
    @staticmethod
    def cut(str_org, start_pos, end_pos, b_start_pos=True, b_end_pos=False):
        if b_start_pos and b_end_pos:
            return str_org[start_pos: end_pos+1]

        if not b_start_pos and b_end_pos:
            return str_org[start_pos+1: end_pos+1]

        if not b_start_pos and not b_end_pos:
            return str_org[start_pos+1: end_pos]

        return str_org[start_pos: end_pos]


    """
    字符串替换
    """
    @staticmethod
    def replace(str_org, str_old, str_new, b_isall=True, r_cnt=0):
        if b_isall:
            return str_org.replace(str_old, str_new)

        return str_org.replace(str_old, str_new, i_cnt)


    """
    字符串搜索
    """
    @staticmethod
    def find(str_org, str_search):
        if str_search:
            return str_search in str_org

        return str_org


    """
    剔除字符串的空格和回车
    """
    @staticmethod
    def strip(str_org,b_left=True, b_right=True):
        if b_left and b_right:
            return str_org.strip()#默认去掉左右空格和回车

        if b_left:
            return str_org.lstrip()#默认去掉左边去空格和回车

        if b_right:
            return str_org.rstrip()#默认去掉右边去空格和回车


    """
    字符大小写转换
    """
    @staticmethod
    def upper_lower(str_org, str_uorl=""):
        if str_uorl == 'L' || str_uorl == 'l':
            return str_org.lower()

        if str_uorl == 'U' || str_uorl == 'u':
            return str_org.upper()

        return str_org













#字符串替换
print("alex li ll".replace('l', 'L', 2)) #替换前两个l为L
print("xxaaxxaa".replace('aa', 'SPAM') #全局替换


name = "My name is alex"
name2 = "My \tname is {name}, age is {age}"
name3 = 2312

print(name[2: 6]) #顾头不顾尾，或左闭右开
print(name.capitalize()) #首字母大写
print(name.ceount('a4')) #统计a字符
print(name.center(50, "-")) #类似格式化输出
print(name.endswith("ex")) #判断是否是ex结尾
print(name.expandtabs(tabsize=30)) #把\t转换成多少个空格
print(name.find("name")) #返回name第一个位置，
print(name[name.find("name"):9]) #可以直接切片
print(name2.format(name="alex", age=23))
print(name2.format_map({"name":"alex","age":32}))
print(name.isalnum()) #是不是一个阿拉伯数字，包含英文字符，0-9数字
print(name.isalpha()) #纯英文字符
print('213'.isdigit()) #是否是整数
print('a1s'.isidentifier()) #判断是不是一个合法的标识符
print('aaa'.islower())
print('bbb'.isupper())
print('231'.isnumeric())
print('df'.isspace())
print("My Name is".istitle()) #第一个字母大写
print("My Name is".isprintable()) #第一个字母大写
print("My name is ".join("==="))
print(", ".join(['1', '2', '3']))
print(name.ljust(50, '*')) #右边填充*
print(name.rjust(50, '-')) #右边填充-
print(name.lower())
print(name.upper())
print("---")
p = str.maketrans("abcdef","123456") #必须长度一样
print("alex li".translate(p)) #p中对应，把alex li里面的字符替换成p对应的，输出:1l5x li

print("alex lil".rfind('l')) #最右边l的下标
print("alex lil".split(' ')) #以空格分割成列表
print("1+2\n+3+4".splitlines()) #识别不同系统的换行
print("Alex lI".swapcase()) #大小字符转换
print("Alex li".title())
print("lex li".zfill(50))
