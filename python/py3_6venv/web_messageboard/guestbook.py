# Author: Jason Lu

import shelve

from datetime import datetime
from flask import Flask, request, render_template, redirect, escape, Markup

app = Flask(__name__)

DATA_FILE = 'guestbook.dat'

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

@app.route('/')
def index():
    greeting_list = load_data()
    return render_template('index.html', greeting_list=greeting_list)


@app.route('/post', methods=['POST'])
def post():

    # 获取已提交的数据
    name = request.form.get('name')
    comment = request.form.get('comment')
    create_at = datetime.now()

    # 保存数据
    save_data(name, comment, create_at)

    # 保存后重定向到首页
    return redirect('/')

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