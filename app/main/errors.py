# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:57
# @Author : LZH
# @File :errors.py
# @software: PyCharm

from flask import render_template
from . import main


@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500