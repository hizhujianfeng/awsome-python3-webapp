#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SMTP 协议测试
smtplib 发送邮件
email 构造邮件
"""

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))




# from_addr = input('From:')
# password = input('Password:')
#
# to_addr = input('To:')
# smtp_server = input('SMTP server:')

from_addr = 'zhujianfeng@tydic.com'
password = 'zjf1223'

to_addr = '2578136777@qq.com'
smtp_server = 'mail.tydic.com'

msg = MIMEMultipart()

msg['From'] = _format_addr('扫地僧<%s>' % from_addr)
msg['To'] = _format_addr('乔峰 <%s>' % to_addr)
msg['Subject'] = Header('天龙八部', 'utf-8').encode()

msg.attach(MIMEText('<html>'
                    '<body>'
                    '阿朱就是阿朱。四海列国，千秋万代，就只有一个阿朱。'
                    '<p><img src="cid:0"></p>'
                    '</body>'
                    '</html>', 'html', 'utf-8'))

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('d://test.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'png', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()