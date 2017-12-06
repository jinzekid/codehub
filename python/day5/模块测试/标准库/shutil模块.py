# Author: Jason Lu

import shutil, os

fs = open("os模块.py", encoding="utf-8")
fd = open("os模块back.txt", "w", encoding="utf-8")

# 复制文件
shutil.copyfileobj(fs, fd)
# shutil.copystat("os模块.py", "222.txt")
shutil.copy("os模块.py", "333.txt")
# 递归的拷贝文件
shutil.copytree("a", "new_a")
# 删除目录
shutil.rmtree("new_a")
# 移动文件
# shutil.move()
# 压缩文件
shutil.make_archive("shutil_archive_test", "zip", root_dir=".")

import zipfile

# os.remove("test_a.zip")
# 压缩
# z = zipfile.ZipFile("test_a.zip", "w")
# z.write("a")
# z.write("os模块.py")
# z.write("111.txt")
# z.close()

# 解压
z = zipfile.ZipFile("test_a.zip", "r")
z.extractall("./test_archive/")
z.close()





















