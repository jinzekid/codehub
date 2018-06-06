# Author: Jason Lu
import json
from bpmappers import Mapper, RawField, DelegateField


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


class UserMapper(Mapper):
    user_id = RawField('id')
    user_nickname = RawField('nickname')

class UserMapper2(UserMapper):
    user_age = RawField('age')

class CommentMapper(Mapper):
    user = DelegateField(UserMapper)
    text = RawField()

def api_user_json(user_id):
    user = get_user(user_id)
    user_dict = UserMapper2(user).as_dict()
    return json.dumps(user_dict, indent=2)

def api_user_detail_json(user_id):
    user = get_user(user_id)
    user_dict = UserMapper2(user).as_dict()
    return json.dumps(user_dict, indent=2)

def api_comment_json(comment_id):
    comment = get_comment(comment_id)
    comment_dict = CommentMapper(comment).as_dict()
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






