# Author: Jason Lu
# 创建蓝本
# 通过实例化一个blueprint类对象可以创建蓝本
# 为什么要使用蓝本
# 在单脚本程序中，程序实例存在于全局作用域中，路由可以直接使用app.route修饰器定义
# 但现在程序在运行时候创建，只有调用create_app()之后才能使用app.route修饰器，
# 这时定义路由和自定义错误页面处理程序就太晚了
# 蓝本中定义的路由处于休眠状态，直到蓝本注册到程序上后，路由才真正成为程序的一部分
# 使用位于全局作用域中的蓝本时，定义路由的方法几乎和单脚本程序一样

from flask import Blueprint
main = Blueprint('main', __name__)

# 导入这两个模块就可以把路由和错误处理程序与蓝本联系起来
# 在末尾导入，避免循环导入依赖
# 因为在views.py, errors.py中还要导入蓝本main
from . import views, errors