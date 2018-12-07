import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtpserver='smtp.163.com'
user='rita_xiaom@163.com'
password='hu199223'

sender='rita_xiaom@163.com'
receives=['2579824719@qq.com','343519661@qq.com']

subject='Web selenium 自动化测试报告'
content='<html><h1>早啊，老朋友！</h1></html>'

send_file=open(r'E:\Photo\fonts_test.png','rb').read()
att=MIMEText(send_file,'base64','utf-8')
att['Content-Type']='application/octet-stream'
att['Content-Disposition']='attachment;filename="fonts_test.png"'

msgRoot=MIMEMultipart()
msgRoot.attach(MIMEText(content,'html','utf-8'))
msgRoot['Subject']=subject
msgRoot['From']=sender
msgRoot['To']=','.join(receives)
msgRoot.attach(att)

smtp=smtplib.SMTP_SSL(smtpserver,465)
smtp.helo(smtpserver)
smtp.ehlo(smtpserver)
smtp.login(user,password)

print('Start send email!')
smtp.sendmail(sender,receives,msgRoot.as_string())
smtp.quit()
print('Send email end! ')