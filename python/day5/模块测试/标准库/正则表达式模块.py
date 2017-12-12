# Author: Jason Lu

import re

'''
五种方法：
match，search，findall，split，sub
'''
ret = re.match("^Chen", "Chen")
print(ret)
ret = re.match("^Chen\d", "Chen123abdc")
print(ret.group()) # 只匹配一个数字
ret = re.match("^Chen\d+", "Chen123abdc发达Chen23")
print(ret.group()) # 只匹配多个数字
ret = re.match(".", "Chen123abdc发达Chen23")
print(ret.group()) # 只匹配一个字母
ret = re.match(".+", "Chen123abdc发达Chen23")
print(ret.group())
# ret = re.match("foo$", "bfoo\nnsfsd")
ret = re.search("foo$", "Chen123fo发达Chen23foo")
print(ret.group()) # 结尾是foo
ret = re.search("^[A-Z]", "Chen123fo发达Chen23foo")
print(ret)
ret = re.search("#.+#", "12#321#hello#")
print(ret)
ret = re.search("aaa?", "aalextaaa")
print(ret) # 匹配aa或者aaa，所以输出aa
ret = re.findall("[0-9]{1,3}", "afda2d34a3243345fdaa")
print(ret) # output: ['2', '34', '324', '334', '5']
ret = re.search("abc|ABC", "ABCBabcCD")
print(ret.group()) # output:ABC
ret = re.findall("abc|ABC", "ABCBabcCD")
print(ret) # output:['ABC', 'abc']
ret = re.search("abc{2}", "alexabccc")
print(ret.group()) # output:abcc
ret = re.search("(abc){2}", "alexabcabccc")
print(ret.group()) # output:abcabc
ret = re.search("(?P<province>[0-9]{4})(?P<city>[0-9]{2})(?P<birthday>[0-9]{4})", "371481199306143242").groupdict("city")
print(ret) # {'province': '3714', 'city': '81', 'birthday': '1993'}
ret = re.split("[0-9]", "abc12de3f")
print(ret) # ['abc', '', 'de', 'f'], 只有一个数字，所有有空格
ret = re.split("[0-9]+", "abc12de3f")
print(ret) # ['abc', 'de', 'f']
ret = re.sub("[0-9]+", "!", "abc12de3f45GH")
print(ret) # output: abc!de!f!GH
ret = re.sub("[0-9]+", "!", "abc12de3f45GH", count=2)
print(ret) # output: abc!de!f45GH
ret = re.search("/", "a/bc/fddfd/\//")
print(ret)





