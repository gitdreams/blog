# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   decorators.py 
# @Time:   2018/6/19 14:05
# 装饰器

from functools import wraps
from flask import g
from .errors import forbidden


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not g.current_user.can(permission):
                return forbidden('权限不足')
            return f(*args, **kwargs)
        return decorated_function
    return decorator