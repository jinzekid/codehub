# Author: Jason Lu
from flask import Flask, render_template, session, flash, url_for, redirect
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(app)

class NameForm(FlaskForm):
    '''
    定义表单累
    包含一个文本字段和一个提交按钮
    '''
    name = StringField('What is your name?',
                       validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')

        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index_flask_wft_4_5.html', form=form,
                           name=session.get('name'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)