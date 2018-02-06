# Author: Jason Lu

import json

class User(object):
    def __init__(self, id, password, nickname, age):
        self.id = id
        self.password = password
        self.nickname = nickname
        self.age = age


class Comment(object):
    def __init__(self, id, user, text):
        self.id = id
        self.user = user
        self.text = text

def get_user(user_id):
    user = User(id=user_id,
                password='hoge',
                nickname='tokibito',
                age=26)
    return user

def get_comment(comment_id):
    comment = Comment(id=comment_id,
                      user=get_user('bp12345'),
                      text=u'Hello, world!')
    return comment

def mapping_user(user):
    return {'user_id': user.id,
            'user_nickname': user.nickname}

def mapping_user_2(user):
    return {'user_id': user.id,
            'user_nickname': user.nickname,
            'user_age': user.age}

def mapping_comment(comment):
    return {'user': mapping_user(comment.user), 'text': comment.text}

def api_user_json(user_id):
    # 以json格式返回用户数据的API
    user = get_user(user_id)
    user_dict = mapping_user(user)
    return json.dumps(user_dict, indent=2)

def api_user_detail_json(user_id):
    # 以json格式返回用户详细数据的API
    user = get_user(user_id)
    user_dict = mapping_user_2(user)
    return json.dumps(user_dict, indent=2)

def api_comment_json(comment_id):
    comment = get_comment(comment_id)
    comment_dict = mapping_comment(comment)
    return json.dumps(comment_dict, indent=2)

def main():
    print('--- api_user_json ---')
    print(api_user_json('bp12345'))
    print()
    print('--- api_user_detail_json ---')
    print(api_user_detail_json('bp12345'))
    print()
    print('--- api_comment_json ---')
    print(api_comment_json('cm54321'))


if __name__ == '__main__':
    main()



