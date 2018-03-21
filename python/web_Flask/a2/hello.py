# Author: Jason Lu
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello world!</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h>'.format(name)

@app.route('/userid/<int:id>')
def userid(id):
    return '<h1>Hello222, {}!</h>'.format(id)

@app.route('/getuseragent')
def get_useragent():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is {}</p>'.format(user_agent)

@app.route('/badrequest')
def get_bad_request():
    return '<h1>Bad Request</h1>', 400


from flask import make_response
@app.route('/makerespnose')
def get_make_response():
    response = make_response('<h1>This is document carries'
                             ' a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# 重定向
from flask import redirect
@app.route('/testredirect')
def get_redirect():
    return redirect('http://www.baidu.com')

# # 处理错误
# from flask import abort
# @app.route('/user_id/<id>')
# def go_user_id():
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return '<h1>Hell, %s</h1>' % user.name

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=7777)