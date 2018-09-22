# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 下午6:58
# @Author  : xxx
# @Site    : 
# @File    : settings.py
# @Software: PyCharm


import os
import platform
import config
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    if platform.system() == 'Linux':
        QR_CODE = 2
    else:
        QR_CODE = False
    TOKEN_CODE = config.TOKEN_CODE
    WEIXIN_GROUP_NAME = config.WEIXIN_GROUP_NAME
    WEIXIN_FRIEND_LIST = config.WEIXIN_FRIEND_LIST
    WEIXIN_FRIEND = config.WEIXIN_FRIEND
