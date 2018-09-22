# -*- coding: utf-8 -*-
# @Time    : 2018/9/22 上午6:52
# @Author  :
# @Site    : 
# @File    : test_example.py
# @Software: PyCharm

#给群组发消息
'''
curl -X POST http://127.0.0.1:5000/gourp/msg/ -d msg="group msg test 9"
'''
import requests

right_token="1234567890"
error_token="123456789011"
IP="127.0.0.1"
PORT="5000"

group_msg_url="http://"+":".join(IP,PORT)+"/gourp/msg/"
failed_post=requests.post(group_msg_url,data={"msg":"gourp","token":error_token})
print(failed_post.json())

success_post=requests.post(group_msg_url,data={"msg":"gourp","token":right_token})
print(success_post.json())


#给朋友们发消息
'''
curl -X POST http://127.0.0.1:5000/friends/msg/ -d msg="z q k l"
'''
friends_msg_url="http://"+":".join(IP,PORT)+"/friends/msg/"
f_p=requests.post(friends_msg_url,data={"msg":"friends","token":error_token})
print(f_p.json())

s_p=requests.post(friends_msg_url,data={"msg":"friends","token":right_token})
print(s_p.json())

#给朋友发消息
'''
curl -X POST http://127.0.0.1:5000/friend/msg/ -d msg="z q k l"
'''
friend_msg_url="http://"+":".join(IP,PORT)+"/friend/msg/"
f_p=requests.post(friend_msg_url,data={"msg":"friend","token":error_token})
print(f_p.json())

s_p=requests.post(friend_msg_url,data={"msg":"friend","token":right_token})
print(s_p.json())