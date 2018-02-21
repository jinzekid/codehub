# Author: Jason Lu

import re
# 普通字符作为原子
pattern = 'yue'
string = "http://yum.iqianyue.com"
result1 = re.search(pattern, string)
print(result1)
print()
# 非打印字符作为原子
# 常用的非打印字符， \n, \t
pattern = "\n"
string = '''http://yum.iqianyue.comhttp://baidu.com'''
result1 = re.search(pattern, string)
print(result1)
print()
# 通用字符作为原子
# 一个原子可以匹配一类字符
# \w 匹配任意一个字母，数字或下划线
# \W 匹配除字母，数字和下划线以外的任意一个字符
# \d 匹配任意一个十进制
# \D 匹配除十进制以外的任意一个其他字符
# \s 匹配任意一个空白字符
# \S 匹配除空白字符以外的任意一个其他字符

pattern = "\w\dpython\w"
string = 'abcdfphp345python_py'
result1 = re.search(pattern, string)
print(result1)
print()
# 原子表
# 可以定义组地位平等的原子，然后匹配的时候会取该原子表中的任意一个原子进行匹配
pattern1 = "\w\dpython[xyz]\w"
pattern2 = "\w\dpython[^xyz]\w" #[^]代表除了括号里面的原子均可以匹配
pattern3 = "\w\dpython[xyz]\W"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
print(result1) # <_sre.SRE_Match object; span=(9, 19), match='45pythony_'>
print(result2) # None
print(result3) # Noe






