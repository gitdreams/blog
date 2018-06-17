# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   __init__.py.py 
# @Time:   2018/6/17 10:43

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views