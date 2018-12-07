import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtpserver='smtp.163.com'

user='rita_xiaom@163.com'
password='hu199223'

sender='rita_xiaom@163.com'
receives=['2579824719@qq.com','343519661@qq.com']

subject='Web selenium 自动化测试报告'
content='<html><h1>早啊，老朋友！</h1></html>'

msg=MIMEText(content,'html','utf-8')
msg['Subject']=Header(subject,'utf-8')
msg['From']='rita_xiaom@163.com'
msg['To']=','.join(receives)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('Start send email!')
smtp.sendmail(sender,receives,msg.as_string())
smtp.quit()
print('Send email end! ')

