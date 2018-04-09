# Author: Jason Lu
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# 定义模型, 一般为Python类
class Role(db.Model):
    __tablename__ = 'roles' #定义在数据库中使用的表名
    id = db.Column(db.Integer, primary_key=True) #
    # db.Colum类构造的第一个参数是数据库列和模型属性的类型
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users' #定义在数据库中使用的表名
    id = db.Column(db.Integer, primary_key=True) #
    # db.Colum类构造的第一个参数是数据库列和模型属性的类型
    username = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username

# if __name__ == '__main__':
#     app2.run(host='0.0.0.0', port=7777, debug=True)