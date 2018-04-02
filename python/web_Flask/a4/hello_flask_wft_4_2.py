# Author: Jason Lu
from flask import Flask, render_template
from flask_wtf import Form
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(Form):
    '''
    定义表单累
    包含一个文本字段和一个提交按钮
    '''
    name = StringField('What is your name?',
                       validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''
    视图函数不仅要渲染表单，还要接收表单中的数据
    :return:
    '''
    name = None
    form = NameForm()
    if form.validate_on_submit(): #调用name字段上附属的DataRequired验证函数
        name = form.name.data #通过字段的data属性获取
        form.name.data = '' #清空表单字段

    return render_template('index_flask_wft_4_2.html', form=form, name=name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)