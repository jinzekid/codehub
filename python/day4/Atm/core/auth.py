# Author: Jason Lu

# 用户认证模块
login_user, login_pwd = "Jason", "abc123"

# 认证装饰器
def auth(auth_type):
    print("auth_type:", auth_type)

    def out_wrapper(func):
        print("func: ", func)

        def inner_wrapper(*args, **kwargs):

            if auth_type == "login":
                print("start login...")
                username = input("Username:").strip()
                password = input("Password:").strip()

                if username == login_user and \
                    password == login_pwd:
                    print("login success...")
                    return func(*args, **kwargs)
                else:
                    exit("\033[32:1mInvalid password or username\033[0m")
            elif auth_type == "logger":
                print("log....")

        return inner_wrapper

    return out_wrapper


@auth(auth_type="login")
def login():
    print("login...")

@auth(auth_type="logger")
def logger():
    print("login...")

# debug
# login()


