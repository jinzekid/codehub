# Author: Jason Lu
from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

# 动态路由
@app.route('/user/<name>')
def user(name):
    return '<h1>hello {}</h1>'.format(name)

# 返回response对象
@app.route('/rep')
def rep():
    response = make_response('<h1>This document carries a cookies!</h1>')
    response.set_cookie('answer', '42')
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


