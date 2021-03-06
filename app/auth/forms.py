# -*- coding:utf-8 _*-  
# @Author: dreams 
# @File:   forms.py 
# @Time:   2018/6/17 10:43

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('邮箱', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码')
    submit = SubmitField('登录')

# 注册表单
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('用户名', validators=[
        DataRequired(),
        Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, '用户名只能由字母，数字，点，下划线组成' )
    ])
    password = PasswordField('密码', validators=[
        DataRequired(),
        EqualTo('confirm', message='两次密码不一致')
    ])
    confirm = PasswordField('确认密码', validators=[
        DataRequired()
    ])
    submit = SubmitField('注册')


    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已经被注册')


    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('该用户已经存在')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('原始密码', validators=[DataRequired()])
    password = PasswordField('新密码', validators=[
        DataRequired(),
        EqualTo('confirm', message='两次密码不一致')
    ])
    confirm = PasswordField('确认新密码', validators=[DataRequired()])
    submit = SubmitField('修改密码')

class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Length(1, 64),
        Email()
    ])
    submit = SubmitField('重置密码')

class PasswordResetForm(FlaskForm):
    password = PasswordField('新密码', validators=[
        DataRequired(),
        EqualTo('confirm', message='两次密码不一致')
    ])
    confirm = PasswordField('确认密码', validators=[DataRequired()])
    submit = SubmitField('重置密码')

class ChangeEmailForm(FlaskForm):
    email = StringField('新邮箱', validators=[
        DataRequired(),
        Length(1, 64),
        Email()
    ])
    password = PasswordField('密码', validators=[DataRequired()])
    submit = SubmitField('修改邮箱')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('邮箱已被注册')