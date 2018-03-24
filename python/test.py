# a = 1
# def fun(a):
#     a = 2
#
# fun(a)
# print(a)
#
# print()
#
# a = []
# def fun2(a):
#     a.append(1)
#
# fun2(a)
# print(a)


# def foo(x):
#     print("executing foo({})".format(x))
#
# class A(object):
#     def foo(self, x):
#         print("executing foo({}, {})".format(self, x))
#
#     @classmethod
#     def class_foo(cls, x):
#         print("executing class_foo({}, {})".format(cls, x))
#
#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo({})".format(x))
#
# a = A()
# a.foo(1)
# a.class_foo(2)
# a.static_foo(3)
#
# A.class_foo(4)
# A.static_foo(5)


# class Person:
#     name = []
#
# p1 = Person()
# p2 = Person()
#
# p1.name.append(1)
# print(p2.name)
#
#
# list = [1,2,3]
# print("list %s" %(list))
# print("list {}".format(list))
#
# # 1.使用__new__方法 ok
# class Singleton(object):
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             orig = super(Singleton, cls)
#             cls._instance = orig.__new__(cls, *args, **kwargs)
#         return cls._instance
#
# class MyClass(Singleton):
#     a = 1
#
# am = MyClass(Singleton())
# am2 = MyClass(Singleton())
# print(id(am))
# print(id(am2))
# print()
# # 2.装饰漆版本 ok
# def singleton(cls, *args, **kwargs):
#     instances = {}
#     def getinstance():
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#     return getinstance
#
# @singleton
# class MyClass3(object):
#     a = 1
#
# a1 = MyClass3()
# a2 = MyClass3()
# print(id(a1))
# print(id(a2))







# # 2.共享属性
# class Borg(object):
#     _state = {}
#     def __new__(cls, *args, **kwargs):
#         ob = super(Borg, cls).__new__(cls, *args, **kwargs)
#         ob.__dict__ = cls._state
#
#         return ob
#
# class MyClass2(Borg):
#     a = 1
#
# b = Borg()
# b2 = Borg()
# print(id(b))
# print(id(b2))


# import urllib.request
# search_key = "中文"
#
# encode_key = urllib.request.quote(search_key)
# encode_url = "https://www.baidu.com/s?wd=%s" % encode_key
# # url编码, 用于中文以及特殊字符
# print(encode_url)
# decode_url = urllib.request.unquote(encode_url)
# print(decode_url)

# file = urllib.request.urlopen("http://www.baidu.com")
# while True:
#     dataline = file.readline()
#     if dataline:
#         print(dataline.decode('utf-8'))
#     else:
#         break
#
# print("end...")








































