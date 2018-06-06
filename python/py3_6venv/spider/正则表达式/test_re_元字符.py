# Author: Jason Lu
# 元字符，就是正则表达式中具有一些特殊含义的字符，比如重复N次前面的字符等
# 常见的元字符以其含义
# .   匹配除换行符以外的任意字符
# ^   匹配字符串的开始位置
# $   匹配字符串的结束位置
# *   匹配0次，1次或多次前面的原子
# ?   匹配0次或1次前面的原子
# +   匹配1次或多次前面的原子
# {n} 前面的原子恰好出现n次
# {n,}前面的原子至少出现n次
# {n,m}   前面的原子至少出现n次，至多出现m次
# |   模式选择符
# ()  模式单元符

import re
pattern = '.python...' # 前面有1位，后面有3位格式的字符(除了换行符以外任意字符)
string = "abcdfphp345python_py"
result1 = re.search(pattern, string)
print(result1)


# 边界限制元字符
# 使用^匹配字符串开始，使用$匹配字符串的结束
pattern1 = "^abd" # 必须以abd开头
pattern2 = "^abc" # 必须以abc开头
pattern3 = "py$" # 必须以py结尾
pattern4 = "ay$" # 必须以ay结尾
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)
if result1 is None:
    print("result1 is none")

# 限定符
# 常见的限定符号*,?,+,{n},{n,},{n,m}
print()
import re
pattern1 = "py.*n"
pattern2 = "cd{2}"
pattern3 = "cd{3}"
pattern4 = "cd{2,}"
string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)
print(result1)
print(result2)
print(result3)
print(result4)

print()
# 模式选择符
import re
pattern = "python|php" #python和php均满足条件
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
print(result1)

print()
# 模式单元符
pattern1 = "(cd){1,}" #cd整体至少出现1次，会尽可能多的匹配
pattern2 = "cd{1,}" #d原子至少出现1次
string = "abcdcdcdcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1) #<_sre.SRE_Match object; span=(2, 10), match='cdcdcdcd'>
print(result2) #<_sre.SRE_Match object; span=(2, 4), match='cd'>

# 模式修正
# 可以在不改变正则表达式的情况下，通过模式修正符改变正则表达式的含义，
# 从而实现一些匹配结果的调整
# I   匹配时候忽略大小写
# M   多行匹配
# L   做本地化识别匹配
# U   根据Unicode字符及解析字符
# S   让.匹配包括换行符，即用了该模式修正后，"."匹配就可以匹配任意的字符了

print()
import re
pattern1 = "python"
pattern2 = "python"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string, re.I)
print(result1) #None
print(result2) #<_sre.SRE_Match object; span=(11, 17), match='Python'>


print()
# 贪婪模式，懒惰模式
import re
pattern1 = "p.*y" # 贪婪模式
pattern2 = "p.*?y" # 懒惰模式
string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1) #<_sre.SRE_Match object; span=(5, 21), match='php345pythony_py'>
print(result2) #<_sre.SRE_Match object; span=(5, 13), match='php345py'>















