# Author: Jason Lu

import re
string = "apythonhellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string)
result2 = re.match(pattern, string).span()
print(result)
print(result2)


print()
import re
string = "pythonhellomypythonhispythonourpythonend"
pattern = ".python."
result = re.match(pattern, string) # 从源字符串的开头进行匹配
result2 = re.search(pattern, string) # 会在全文中进行检索匹配
print(result) #None
print(result2) #<_sre.SRE_Match object; span=(12, 20), match='ypythonh'>


print()
# 全局匹配函数
# 源字符串中有多个结果符合模式，希望符合模式的内容全部都匹配出来
# 1.使用re.complie()对正则表达式进行预编译
# 2.编译后，使用finall()根据正则表达式从源字符串中将匹配的结果全部找出
import re
string = "hellomypythonhispythonourpythonend"
pattern = re.compile(".python.") #预编译
result = pattern.findall(string) # 找出符合模式的所有结果
print(result) #['ypythonh', 'spythono', 'rpythone']


print()
# 根据正则表达式来实现替换某些字符串的功能
# 使用re.sub函数实现
import re
string = "hellomypythonhispythonoutpythonend"
pattern = "python."
result1 = re.sub(pattern, "php", string) #全部替换
result2 = re.sub(pattern, "php", string, 2) #最多地替换2次
print(result1) #hellomyphpisphputphpnd
print(result2) #hellomyphpisphputpythonend


print()
# 常见实例
# 匹配网址
import re
pattern = "[a-zA-Z]+://[^\s]*[.com|.cn]"
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result) #<_sre.SRE_Match object; span=(9, 29), match='http://www.baidu.com'>

# 匹配电话号码
import re
pattern = "\d{4}-\d{7}|\d{3}-\d{8}" # 匹配电话号码的正则表达式
string = "021-672826353682382265236"
result = re.search(pattern, string)
print(result) #<_sre.SRE_Match object; span=(0, 12), match='021-67282635'>

# 匹配电子邮件
import re
pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"
string = "<\a href='http://www.baidu.com'>百度首页<\/a><br><\a href='mailto:c-e+o@iqi-anyue.com.cn'>电子邮件地址<\/a>"
result = re.search(pattern, string)
print(result) #<_sre.SRE_Match object; span=(59, 81), match='c-e+o@iqi-anyue.com.cn'>



