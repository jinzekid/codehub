# Author: Jason Lu
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    '''
    定义表单累
    包含一个文本字段和一个提交按钮
    '''
    name = StringField('What is your name?',
                       validators=[DataRequired()])
    submit = SubmitField('Submit')