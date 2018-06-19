# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   errors.py 
# @Time:   2018/6/19 14:06

from flask import jsonify
from app.exceptions import ValidationError
from . import api


def bad_request(message):
    response = jsonify(
        {
            'error': '错误请求',
            'message': message
        }
    )
    response.status_code = 400
    return response


def unauthorized(message):
    response = jsonify(
        {
            'error': '未认证',
            'message': message
        }
    )
    response.status_code = 401
    return response


def forbidden(message):
    response = jsonify(
        {
            'error': '被禁止',
            'message': message
        }
    )
    response.status_code = 403
    return response


@api.errorhandler(ValidationError)
def valildation_error(e):
    return bad_request(e.args[0])
