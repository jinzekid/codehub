# Author: Jason Lu

print("\n============字典转换============\n")
dict = {
        "name": "Zara",
        "age": 7,
        "class": "111"
        }

# 字典--》字符串
print("字典--》字符串 ", type(dict), str(dict))
# 字典key--》元组
print("字典key--》元组 ", tuple(dict))
# 字典value--》元组
print("字典value--》元组 ", tuple(dict.values()))
# 字典key--》列表
print("字典key--》列表 ", list(dict))

print("\n============元组转换============\n")
tup = (1, 2, 3, 4, 5)

# 元组--》字符串
print("元组--》字符串 ", str(tup))
# 元组--》列表
print("元组--》列表 ", list(tup))

print("\n============列表转换============\n")
nums = [1, 3, 5, 7, 8, 13, 20]

# 列表--》字符串
print("列表--》字符串 ", str(nums))
# 列表--》元组
print("列表--》元组 ", tuple(nums))

print("\n============字符串转换============\n")
str = "(1, 2, 3)"

# 字符串--》元组
print("字符串--》元组 ", tuple(eval(str)))
# 字符串--》列表
print("字符串--》列表 ", list(eval(str)))
# 字符串--》字典
str_dic = "{'name':'ljq', 'age':24}"
print(eval(str_dic))


