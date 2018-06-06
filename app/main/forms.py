# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:57
# @Author : LZH
# @File :forms.py
# @software: PyCharm
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class NameForm(FlaskForm)
    naem = StringField('what is your name?', validators=[DataRequired])
    submit = SubmitField('Submit')