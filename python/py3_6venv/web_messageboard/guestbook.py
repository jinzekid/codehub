# Author: Jason Lu

import shelve

from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup, make_response
from flask import jsonify, url_for, abort, make_response
from bpmappers import Mapper, RawField, ListDelegateField

app = Flask(__name__)
app.config['DEBUG'] = True
# app.config.update()

DATA_FILE = 'guestbook.dat'

###################### 相关方法 ######################
def save_data(name, comment, create_at):
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)

    # 如果数据库中没有greeting_list，就新建一个表
    if 'greeting_list' not in database:
        greeting_list = []
    else:
        # 从数据库获取数据
        greeting_list = database['greeting_list']

    # 将提交的数据添加到表头
    greeting_list.insert(0, {
        'name': name,
        'comment': comment,
        'create_at': create_at
    })

    # 更新数据库
    database['greeting_list'] = greeting_list
    # 关闭数据库
    database.close()

def load_data():
    # 通过shelve模块打开数据库文件
    database = shelve.open(DATA_FILE)
    # 返回greeting_list,如果没有数据则返回空表
    greeting_list = database.get('greeting_list', [])
    database.close()
    return greeting_list


###################### 相关类 ######################
class GreetingMapper(Mapper):
    name = RawField()
    comment = RawField()

class GreetingListMapper(Mapper):
    greeting_list = ListDelegateField(GreetingMapper)


###################### 路由地址 ######################
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    return resp

# 登陆页面
@app.route('/login/')
def page_login():
    return render_template('login.html')

# 留言板首页
@app.route('/')
def page_index():
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)

@app.route('/api/')
def api_index():
    # 留言
    greeting_list = load_data()
    result_dict = GreetingListMapper({'greeting_list': greeting_list}).as_dict()
    return jsonify(**result_dict)

# 动态url抽象成一个url模式
@app.route('/item/<id>/')
def item(id):
    return 'Item: {}'.format(id)

# 访问/a和/b都符合这个规则
@app.route('/<any(a, b):page_name>/')
def pageAB(page_name):
    return page_name

@app.route('/j/item/<id>', methods=['DELETE', 'POST'])
def getItem(id):
    return id

# 构造URL
@app.route('/newurl/1/')
def item2():
    return url_for('item', id=2, aid='/') #output:/item/2/?aid=%2F

@app.route('/secret/')
def secret():
    abort(401)
    print('This is never executed')

###################### 请求方法 ######################
# 登陆请求
@app.route('/post_tologin', methods=['GET', 'POST'])
def do_login():
    if request.method == 'POST':
        # 获取登陆表单的用户名和密码
        username = request.form.get('username')
        password = request.form.get('password')

    if username == 'lu' and password == '123':
        # 保存后重定向到首页
        return redirect('/')
    else:
        # 保存后重定向到首页
        return redirect('/login/')


@app.route('/post_comment', methods=['POST'])
def post_comment():

    # 获取已提交的数据
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()

    # 保存数据
    save_data(name, comment, create_at)

    # 保存后重定向到首页
    return redirect('/')


###################### 其他功能 ######################
@app.template_filter('nl2br')
def nl2br_filter(s):
    # 将换行符置换为br标签的模版过滤器
    return escape(s).replace('\n', Markup('<br>'))

@app.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
    # 使datetime对象更容易分辨的模版过滤器
    return dt.strftime('%Y/%m/%d %H:%M:%S')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)