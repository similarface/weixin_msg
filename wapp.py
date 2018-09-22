# -*- coding: utf-8 -*-
from flask import Flask, jsonify, request, url_for, redirect
from weixin_chart import WX
from settings import ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

# 初始化微信
weixin = WX(console_qr=app.config.get('QR_CODE'))

token = "1234567890"

from selflogger import logger

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


@app.route('/gourp/msg/', methods=['POST'])
def group_msg():
    '''
    给群发消息
    :return:
    '''
    if request.method == 'POST':
        token = request.form.get('token')
        print(token)
        if token == app.config.get('TOKEN_CODE'):
            msg = request.form.get('msg')
            group = app.config.get('WEIXIN_GROUP_NAME')
            try:
                flag = weixin.group_msg(group, msg)
                if flag:
                    return jsonify({"code": 0, "data": None, "msg": "SUCCESS"})
                else:
                    return jsonify({"code": 1, "data": [flag], "msg": "ERROR"})
            except Exception as e:
                logger.error(e)
                return jsonify({"code": 1, "data": [{"error":e,"msg":msg}], "msg": "ERROR"})
        else:
            return jsonify( {"code": 1, "data": [{"token":token}], "msg": "token error"})
    else:
        return jsonify({"code": 1, 'data': None, 'msg': 'Method{} Not Allowed!'.format(request.method)})


@app.route('/friends/msg/', methods=['POST'])
def friends_msg():
    '''
    给配置的多个朋友发消息
    :return:
    '''
    if request.method == 'POST':
        token = request.form.get('token')
        if token == app.config.get('TOKEN_CODE'):
            msg = request.form.get('msg')
            friends = app.config.get('WEIXIN_FRIEND_LIST')
            try:
                flag = weixin.many_friend_msg(friends, msg)
                if flag:
                    return jsonify({"code": 0, "data": None, "msg": "SUCCESS"})
                else:
                    return jsonify({"code": 1, "data": [flag], "msg": "ERROR"})
            except Exception as e:
                logger.error(e)
                return jsonify({"code": 1, "data": [{"error":e,"msg":msg}], "msg": "ERROR"})
        else:
            return jsonify( {"code": 1, "data": [{"token":token}], "msg": "token error"})
    else:
        return jsonify({"code": 1, 'data': None, 'msg': 'Method{} Not Allowed!'.format(request.method)})


@app.route('/friend/msg/', methods=['POST'])
def friend_msg():
    '''
    给配置的一个朋友发消息
    :return:
    '''
    if request.method == 'POST':
        token = request.form.get('token')
        if token == app.config.get('TOKEN_CODE'):
            msg = request.form.get('msg')
            friend = app.config.get('WEIXIN_FRIEND')
            try:
                flag = weixin.friend_msg(friend, msg)
                if flag:
                    return jsonify({"code": 0, "data": None, "msg": "SUCCESS"})
                else:
                    return jsonify({"code": 1, "data": [flag], "msg": "ERROR"})
            except Exception as e:
                logger.error(e)
                return jsonify({"code": 1, "data": [{"error":e,"msg":msg}], "msg": "ERROR"})
        else:
            return jsonify( {"code": 1, "data": [{"token":token}], "msg": "token error"})
    else:
        return jsonify({"code": 1, 'data': None, 'msg': 'Method{} Not Allowed!'.format(request.method)})

