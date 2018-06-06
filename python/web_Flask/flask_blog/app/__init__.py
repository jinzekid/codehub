#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_login import LoginManager

bootstrap   = Bootstrap()
mail        = Mail()
moment      = Moment()
db          = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

# 程序的工厂函数
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    # 在工厂函数中注册蓝本
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    # url_prefix,在注册后蓝本中定义的所有路由都会加上指定的前缀，即这个例子中/auth
    # /login路由会注册成/auth/login
    # 在web开发中，完整的url:http://localhost:5000/auth/login
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # 附加路由和自定义的错误页面

    return app