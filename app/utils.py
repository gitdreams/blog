# -*- coding: utf-8 -*-
# @Time :2018/6/6 10:04
# @Author : LZH
# @File :utils.py
# @software: PyCharm

import time

from flask import url_for as _url_for, current_app, _request_ctx_stack

def timestamp():
    return int(time.time())

def url_for(*args, **kwargs):
    if '_external' not in kwargs:
        kwargs['_external'] = False
    reqctx = _request_ctx_stack.top
    if reqctx is None:
        if kwargs['_external']:
            raise RuntimeError('Cannot generate external URLS without a request context.')
        with current_app.test_request_context():
            return _url_for(*args, **kwargs)
    return _url_for(*args, **kwargs)