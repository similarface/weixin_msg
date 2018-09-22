# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 上午4:31
# @Author  :
# @Site    : 
# @File    : config.py
# @Software: PyCharm
import os
try:
    import configparser as ConfigParser
except ImportError:
    import ConfigParser

cf = ConfigParser.ConfigParser()
#本机mac
cf.read(os.path.join(os.path.join(os.path.dirname(__file__),"config.ini")))


mailto_list =[_.strip() for _ in cf.get('email','mailto_list').strip().split(',')]
mail_host = cf.get('email','mail_host')
mail_user = cf.get('email','mail_user')
mail_pass = cf.get('email','mail_pass')
mail_postfix = cf.get('email','mail_postfix')


TOKEN_CODE = cf.get('weixin','TOKEN_CODE')
WEIXIN_GROUP_NAME = cf.get('weixin','WEIXIN_GROUP_NAME')
WEIXIN_FRIEND_LIST = [_.strip() for _ in cf.get('weixin','WEIXIN_FRIEND_LIST').split(",")]
WEIXIN_FRIEND = cf.get('weixin','WEIXIN_FRIEND')
