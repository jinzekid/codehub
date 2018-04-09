#!/usr/bin/python
# -*- coding:utf-8 -*-

import os
from app import create_app, db
from app.models import User, Role
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

# 如果已经定义了环境变量FLASK_CONFIG,则从中读取配置名，否则使用默认配置
app     = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    '''Run the unit tests.'''
    import unittest
	tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

def test2():
	pinrt("this is test fun")

def __str__(self):
    print("%s", __name__)


# 脚本中加入shebang声明，所以在unix中可以通过./manage.py执行脚本
if __name__ == '__main__':
    manager.run()
