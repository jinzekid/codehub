# Author: Jason Lu
from flask import Flask, render_template, session, redirect, url_for
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(Form):
    '''
    定义表单累
    包含一个文本字段和一个提交按钮
    '''
    name = StringField('What is your name?',
                       validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.route('/', methods=['Get', 'Post'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data #保存变量
        # 这里的重定向本来可以写成，redirect('/'),
        # 但却会使用Flask提供的URL生成函数url_for()
        # 推荐使用url_for生成URL, 因为这个函数使用URL映射生成URL,
        # 从而保证URL和定义的路由兼容
        # 而且修改路由名字后依然可用
        return redirect(url_for('index'))

    return render_template('index_flask_wft_4_2.html', form=form,
                           name=session.get('name'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)