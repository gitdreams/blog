# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   __init__.py.py 
# @Time:   2018/6/19 14:04

from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
