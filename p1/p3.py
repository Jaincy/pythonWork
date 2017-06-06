#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


my_sender = '13676924256@163.com'  # 发件人邮箱账号
my_pass = 'd123526'  # 发件人邮箱密码
my_receive = '609447971@qq.com'  # 收件人邮箱账号，我这边发送给自己

# 创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

# 邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('./test.txt', 'rb').read(), 'plain', 'utf-8')
message.attach(att1)

# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="./test.txt"'
# message.attach(att1)

smtpObj = smtplib.SMTP("smtp.163.com", 25)
smtpObj.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
smtpObj.sendmail(my_sender, [my_receive, ], message.as_string())
