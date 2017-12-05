# Author: Jason Lu

import time
user, passwd = "alex", "abc123"
def auth(auth_type):
    print("auth func: ", auth_type)
    def outer_wrapper(func):
        print("func is: %s", func)
        def wrapper(*args, **kwargs):
            print("args: %s, kwargs: %s", args, kwargs)
            # 根据不同的验证输入
            if auth_type == "local":
                username = input("Username:").strip()
                password = input("Password:").strip()

                if username == user and \
                                password == passwd:
                    print("\033[32:1mUser has passed authentication\033[0m")
                    # 如果有返回值，就需要添加return
                    return func(*args, **kwargs)
                else:
                    exit("\033[32:1mInvalid password or username\033[0m")
            elif auth_type == "ldap":
                print("不会ldap....")

        return wrapper

    return outer_wrapper


def index():
    print("Welcome to index page")

@auth(auth_type="local")
def home():
    print("Welcome to home page")
    return "from home"

@auth(auth_type="ldap")
def bbs():
    print("welcome to bbs page")

# index()
print(home())
bbs()