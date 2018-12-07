import smtplib
from email.mime.text import MIMEText
from email.header import Header
#调用服务器
smtpserver='smtp.163.com'
#用户名和密码
user='rita_xiaom@163.com'
password='hu199223'
#发送和接收账号
sender='rita_xiaom@163.com'
receive='2579824719@qq.com'

#构造邮件
subject='Web selenium 自动化测试报告'
content='<html><h1>早啊，老朋友！</h1></html>'
#编码设置格式
msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='rita_xiaom@163.com'
msg['To']='2579824719@qq.com'

#与服务器交互
smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

#发送邮件
print('Start send email!')
smtp.sendmail(sender,receive,msg.as_string())
smtp.quit()
print('Send email end! ')