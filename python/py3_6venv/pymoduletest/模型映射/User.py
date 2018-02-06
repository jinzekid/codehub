# Author: Jason Lu

class User(object):
    def __init__(self, id, password, nickname, age):
        self.id = id
        self.password = password
        self.nickname = nickname
        self.age = age


import json

def convert_user_to_json(user):
    # 获取一个User对象并返回Json
    user_dict = {
        'user_id': user.id,
        'user_nickname': user.nickname
    }
    return json.dumps(user_dict)


