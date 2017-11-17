# Author: Jason Lu

name = "My \tname is alex"
name2 = "My \tname is {name}, age is {age}"
name3 = 2312

print(name.capitalize()) #首字母大写
print(name.count('a')) #统计a字符
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
print(", ".join(['1','2','3']))
print(name.ljust(50,'*')) #右边填充*
print(name.rjust(50,'-')) #右边填充-
print(name.lower())
print(name.upper())
print("\nAlex\n".lstrip()) #默认去掉左边去空格和回车
print("\nAlex\n".rstrip()) #默认去掉右边去空格和回车
print("\nAlex\n".strip()) #默认去掉左，右边去空格和回车
print("---")
p = str.maketrans("abcdef","123456") #必须长度一样
print("alex li".translate(p)) #p中对应，把alex li里面的字符替换成p对应的，输出:1l5x li

print("alex li ll".replace('l', 'L', 2)) #替换前两个l为L
print("alex lil".rfind('l')) #最右边l的下标
print("alex lil".split(' ')) #以空格分割成列表
print("1+2\n+3+4".splitlines()) #识别不同系统的换行
print("Alex lI".swapcase()) #大小字符转换
print("Alex li".title())
print("lex li".zfill(50))