# Author: Jason Lu

def bulk(self):
    print("%s is yelling..." %(self.name))

class Dog(object):

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("%s is eating..." %(self.name))


d = Dog("alex")
# choice = input(">>>:").strip()


# 异常处理
names = ["alex", "jack"]
data = {}
try:
    data["name"]
    # names[3]
except KeyError as e:
    print("没有这个key: ", e)
except EOFError as e:
    print("Index error：", e)
except IndexError as e:
    print("Index error：", e)
finally:
    print("finally except")

'''
except (KeyError, IndexError) as e: # 当统一处理错误方法，可以有这种写法
    print("没有这个key:", e)
except EOFError as e:
    print("Index error：", e)
'''

# 自定义异常
class JasonException(Exception):

    def __init__(self, msg):
        self.message = msg

    # 返回e的内容， 可以不写
    '''
    def __str__(self):
        return "这是测试"
    '''

try:
    raise JasonException("我的异常")
except JasonException as e:
    print(e)
