# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:57
# @Author : LZH
# @File :forms.py
# @software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp
from wtforms import ValidationError
from flask_pagedown.fields import PageDownField
from ..models import Role, User


class NameForm(FlaskForm):
    name = StringField('你的名字', validators=[DataRequired()])
    submit = SubmitField('提交')


class EditProfileForm(FlaskForm):
    name = StringField('真实姓名', validators=[Length(0, 64)])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = SubmitField('提交')

class EditProfileAdminForm(FlaskForm):
    email = StringField('邮件', validators=[
        DataRequired(),
        Length(0, 64),
        Email()
    ])
    username = StringField('用户名', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A_Za-z0-9_.]*$', 0,
               '用户名必须是字母数字或者点好和下划线组成')
    ])
    confirmed = BooleanField('确认')
    role = SelectField('角色', coerce=int)
    name = StringField('角色名称', validators=[Length(0, 64)])
    location = StringField('位置', validators=[Length(0, 64)])
    about_me = TextAreaField('简介')
    submit = StringField('提交')

    def __init__(self, user, *args, **kwargs):
        super(EditProfileAdminForm, self).__init__(*args, **kwargs)
        self.role.choices = [(role.id, role.name)
                             for role in Role.query.order_by(Role.name).all()]
        self.user = user

    def validate_email(self, field):
        if field.data != self.user.email and \
                User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')

    def validate_username(self, field):
        if field.data != self.user.username and \
                User.query.filter_by(username=field.data).first():
            raise ValidationError('用户名已经存在')


class PostForm(FlaskForm):
    body = PageDownField('你的想法是什么？', validators=[DataRequired()])
    submit = SubmitField('提交')


class CommentForm(FlaskForm):
    body = StringField('输入你的评论', validators=[DataRequired()])
    submit = SubmitField('提交')
