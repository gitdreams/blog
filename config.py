# -*- coding: utf-8 -*-
# @Time :2018/3/13 20:53
# @Author : LZH
# @File :config.py
# @software: PyCharm

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'hard to guess string'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_PORT = 465
    MAIL_DEBUG = True
    MAIL_USERNAME = '120735429@qq.com'
    MAIL_PASSWORD = 'cmifzzyxnfmtbidd'
    FLASKY_MAIL_SENDER = '120735429@qq.com'
    FLASKY_ADMIN = '120735429@qq.com'
    SSL_REDIRECT = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
    FLASKY_POSTS_PER_PAGE = 20
    FLASKY_FOLLOWERS_PER_PAGE = 50
    FLASKY_COMMENTS_PER_PAGE = 30
    FLASKY_SLOW_DB_QUERY_TIME = 0.5
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:111111@localhost/maildb'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    # MAIL_SERVER = 'smtp.qq.com'
    # MAIL_PORT = 465
    # MAIL_USE_SSL = True
    # MAIL_USE_TLS = False
    # MAIL_USERNAME = '120735429@qq.com'
    # MAIL_PASSWORD = 'cmifzzyxnfmtbidd'
    # SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:111111@localhost/maildb'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:111111@localhost/maildb'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:111111@localhost/maildb'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
