# Author: Jason Lu
# 创建认证蓝本
# 使用蓝本在全局作用域中定义路由
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views