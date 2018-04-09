# Author: Jason Lu
import os, time
print(os.chdir("/Users/jasonlu/Desktop/")) # 切换成当前路径
print(os.getcwd())
print(os.pardir)
# print(os.stat())
# os.makedirs("/Users/jasonlu/Desktop/test") # 创建目录, 能够递归的建立目录
# os.removedirs("/Users/jasonlu/Desktop/test") # 移除目录，递归的删除
# os.mkdir("/Users/jasonlu/Desktop/test") # 创建目录，不递归
# os.rmdir("/Users/jasonlu/Desktop/test") # 删除目录，不递归
# os.renames("oldname", "newname")
# os.listdir("/Users/jasonlu/Desktop/") # 文件中的文件列表
# os.stat("/Users/jasonlu/Desktop/thefile.txt") # 文本信息
print(os.sep)
print(os.linesep)
print(os.pathsep)
print(os.environ) # 查看当前系统的环境变量
print(os.name)
print(os.system("ls"))
print(os.path.abspath("."))

path = os.path.abspath(".")
print(os.path.split(path)) # ('/Users/jasonlu', 'Desktop')
print(os.path.dirname("/Users/jasonlu/Desktop/thefile.txt")) # 获取文件路径名

if os.path.exists("/Users/jasonlu/Desktop"):
    print("true")
else:
    print("false")

print(os.path.isabs("/Users/jasonlu/Desktop/Dev")) # 以根开头的，/ 绝对路径
print(os.path.isfile("/Users/jasonlu/Desktop/thefile.txt")) # 判断是否是文件
print(os.path.isdir("/Users/jasonlu/Desktop/")) # 是否是目录

path = os.path.join("/Users/jasonlu/Desktop/", "a4", "b", "a4.txt")
print(path)
print(os.path.getatime("/Users/jasonlu/Desktop/thefile.txt")) # 创建时间
changetime = time.gmtime(os.path.getctime("/Users/jasonlu/Desktop/thefile.txt"))
print(changetime)
# print(os.path.getctime("/Users/jasonlu/Desktop/thefile.txt")) # 修改时间





































