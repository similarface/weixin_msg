# -*- coding: utf-8 -*-
# @Time    : 2018/9/21 下午8:06
# @Author  : xxx
# @Site    : 
# @File    : weixin_chart.py
# @Software: PyCharm
import sys

from wxpy import *
from selflogger import logger
from config import mailto_list

from SMTPEmail import send_mailWithAttachments

class WX:
    def __init__(self,console_qr=False, cache_path=True, qr_png='./qr_png.png'):
        self.bot = Bot(console_qr=console_qr,cache_path=cache_path, qr_path=qr_png)

    def get_friend(self, friend):
        my_friend = self.bot.friends().search(friend)
        return my_friend

    def group_msg(self, group, msg):
        '''
        群发消息
        :param group:
        :param msg:
        :return:
        '''
        logger.info("send msg to group{}".format(group))
        my_group = ensure_one(self.bot.groups().search(group))
        my_group.send_msg(msg)
        return True

    def friend_msg(self, friend, msg):
        '''
        一个朋友发消息
        :param friend:
        :param msg:
        :return:
        '''
        f = ensure_one(self.bot.friends().search(friend))
        f.send_msg(msg)
        return True

    def many_friend_msg(self, friendes, msg):
        '''
        多个朋友发消息
        :param friendes:
        :param msg:
        :return:
        '''
        if isinstance(friendes,list):
            for friende in friendes:
                self.friend_msg(friende,msg)
            return True
        else:
            raise TypeError('expected list, {} found'.format(type(friendes)))

    def many_friend_group_msg(self, friendes, msg):
        '''
        多个朋友发消息
        :param friendes:
        :param msg:
        :return:
        '''
        g = self.bot.create_group(friendes,'zqjkl')
        g.send_msg(msg)
        return True


