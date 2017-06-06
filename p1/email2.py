# encoding=utf-8
import os.path
import smtplib

import email.MIMEBase

From = "13676924256@163.com"
To = "13676924256@163.com"
file_name = "./img/qq.jpg"

server = smtplib.SMTP("smtp.163.com")
server.login("13676924256@163.com", "d123526")  # 仅smtp服务器需要验证时

# 构造MIMEMultipart对象做为根容器
main_msg = email.MIMEMultipart.MIMEMultipart()

# 构造MIMEText对象做为邮件显示内容并附加到根容器
text_msg = email.MIMEText.MIMEText("this is a test text to text mime")
main_msg.attach(text_msg)

# 构造MIMEBase对象做为文件附件内容并附加到根容器
contype = 'application/octet-stream'
maintype, subtype = contype.split('/', 1)

# 读入文件内容并格式化
data = open(file_name, 'rb')
file_msg = email.MIMEBase.MIMEBase(maintype, subtype)
file_msg.set_payload(data.read())
data.close()
email.Encoders.encode_base64(file_msg)

# 设置附件头
basename = os.path.basename(file_name)
file_msg.add_header('Content-Disposition',
                    'attachment', filename=basename)
main_msg.attach(file_msg)

# 设置根容器属性
main_msg['From'] = From
main_msg['To'] = To
main_msg['Subject'] = "美美的 "
main_msg['Date'] = email.Utils.formatdate()

# 得到格式化后的完整文本
fullText = main_msg.as_string()

# 用smtp发送邮件

try:
    server.sendmail(From, To, fullText)
finally:
    server.quit()
