# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 上午6:44
# @Author  :
# @Site    : 
# @File    : main.py
# @Software: PyCharm

from wapp import app
from flask_script import Manager

manager = Manager(app)

if __name__ == '__main__':
    manager.run()