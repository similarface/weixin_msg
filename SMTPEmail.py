# -*- coding:utf-8 -*-
import datetime
import random

__author__ = ''
'''
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议
它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。
python的smtplib提供了一种很方便的途径发送电子邮件。
它对smtp协议进行了简单的封装。
Python创建 SMTP 对象语法如下：
    import smtplib
    smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )
参数说明：
    host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cc，这个是可选参数。
    port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
    local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。

Python SMTP对象使用sendmail方法发送邮件，语法如下：
    SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]
参数说明：
    from_addr: 邮件发送者地址。
    to_addrs: 字符串列表，邮件发送地址。
    msg: 发送消息
    这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config import mailto_list, mail_host, mail_user, mail_pass, mail_postfix


def send_mail(to_list, sub, content):
    '''
    to_list：收件人；
    sub：主题；
    content：邮件内容
    '''
    # 这里的hello可以任意设置，收到信后，将按照设置显示
    me = "MZCF maybe problem" + "<" + mail_user + "@" + mail_postfix + ">"
    # 创建一个实例，这里设置为html格式邮件
    msg = MIMEText(content, _subtype='html', _charset='UTF-8')
    # 设置主题
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        # 连接smtp服务器
        s.connect(mail_host)
        # 登陆服务器
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(me, to_list, msg.as_string())

        s.close()
        return True
    except Exception as e:
        print(e)
        return False


def send_mailWithAttachments(sub, pngfile):
    '''
    #带附件邮件的发送
    :param to_list:收件人
    :param sub:主题
    :param conent:内容，现在是个panda DF
    :return:
    '''
    to_list = mailto_list
    # 创建一个带附件的实例
    Mail_attachments_msg = MIMEMultipart()
    # 够造附件1
    att1 = MIMEText(open(pngfile, 'rb').read(), 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'wexin qr; filename="{}"'.format(pngfile)
    Mail_attachments_msg.attach(att1)
    me = "weixin qr code" + "<" + mail_user + "@" + mail_postfix + ">"
    # 设置主题
    Mail_attachments_msg['Subject'] = sub
    Mail_attachments_msg['From'] = me
    Mail_attachments_msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        # 连接smtp服务器
        s.connect(mail_host)
        # 登陆服务器
        s.login(mail_user, mail_pass)
        # 发送邮件
        s.sendmail(me, to_list, Mail_attachments_msg.as_string())
        s.quit()
        return True
    except Exception as e:
        return False


if __name__ == '__main__':
    print(mailto_list)
    if send_mail(mailto_list, "ppp","OK"):
        print("发送成功")
    else:
        print("发送失败")
