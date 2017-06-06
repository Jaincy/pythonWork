#! /usr/bin/env python
# encoding=utf-8

import email.MIMEMultipart
import email.MIMEText
import email.MIMEBase
import base64
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '13676924256@163.com'  # 发件人邮箱账号
my_pass = 'd123526'  # 发件人邮箱密码
my_user = '13676924256@163.com'  # 收件人邮箱账号，我这边发送给自己


def mail(content):
    ret = True
    try:

    

        # msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        # msg = MIMEText(base64.b64encode(open('C:\Users\dell、\Downloads\\test.txt', 'rb').read()), 'plain', 'utf-8')
        # msg = MIMEText(base64.b64encode(open(content).read()), 'plain', 'utf-8')
        msg = MIMEText(open(content).read(), 'plain', 'utf-8')
        msg = M
        msg['From'] = formataddr(["FromRunoob", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["FK", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP("smtp.163.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码

        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
        print "失败"
    return ret


if __name__ == '__main__':
    ret = mail("./log/keyboard/2017-06-06.txt")

    if ret:
        print("邮件发送成功")
        print base64.b64decode("cXFx")
    else:
        print("邮件发送失败")
