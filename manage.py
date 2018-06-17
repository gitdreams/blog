# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:56
# @Author : LZH
# @File :manage.py
# @software: PyCharm

from app import create_app, db
import os

from config import Config
app = create_app(os.getenv('FLASK_Config') or 'default')
# app.config.from_object(Config)
app.app_context()
app.app_context().push()
# with app.app_context():
#     db.create_all()

app.run(debug=False)