# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:56
# @Author : LZH
# @File :manage.py
# @software: PyCharm

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from twisted.web import server
from twisted.web.wsgi import WSGIResource
from flask_script import Manager
from twisted.internet import reactor

from app import create_app, db
import os
from config import Config
from app.models import *

app = create_app(os.getenv('FLASK_Config') or 'default')
manager = Manager(app)
app.app_context()
app.app_context().push()
# with app.app_context():
#     db.create_all()
#
# from app.models import Role
# Role.insert_roles()

app.run()
# manager.run()

# app.run(debug=False)