# -*- coding: utf-8 -*-
# @Time :2018/3/17 20:33
# @Author : LZH
# @File :email.py
# @software: PyCharm

from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from . import mail


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(to, subject, template, **kwargs):
    print(to, subject, template)
    app = current_app._get_current_object()
    msg = Message(subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
