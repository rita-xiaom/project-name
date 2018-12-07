#带附件的测试报告发送
import unittest
from BSTestRunner import BSTestRunner
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()

    smtpserver = 'smtp.163.com'
    user = 'rita_xiaom@163.com'
    password = 'hu199223'

    sender = 'rita_xiaom@163.com'
    receives = ['2579824719@qq.com', '343519661@qq.com']

    subject = 'Web selenium 自动化测试报告'
    # content = '<html><h1>早啊，老朋友！</h1></html>'

    send_file = open(r'E:\Photo\fonts_test.png', 'rb').read()
    att = MIMEText(send_file, 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="fonts_test.png"'

    msgRoot = MIMEMultipart()
    msgRoot.attach(MIMEText(mail_content, 'html', 'utf-8'))
    msgRoot['Subject'] = subject
    msgRoot['From'] = sender
    msgRoot['To'] = ','.join(receives)
    msgRoot.attach(att)

    smtp = smtplib.SMTP_SSL(smtpserver, 465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(user, password)

    print('Start send email!')
    smtp.sendmail(sender, receives, msgRoot.as_string())
    smtp.quit()
    print('Send email end! ')

def last_report(report_dir):
    lists = os.listdir(report_dir)
    # print(lists)
    # sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，
    # 获取文件的最后修改时间，所以最终以文件时间从小到大排序
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getatime(report_dir + '\\' + fn))
    # print("the latest report is " + lists[-1])
    # 获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名
    file = os.path.join(report_dir, lists[-1])
    # print(file)
    return file

if __name__ == '__main__':
    report_dir='./test_report'
    test_dir = './test_case'
    discovery = unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    report_name=report_dir+'/'+now+' result.html'

    with open(report_name,'wb')as f:
        runner=BSTestRunner(stream=f,title="Test Report",description='test  case result')
        runner.run(discovery)
    f.close()

    last_report=last_report(report_dir)
    send_mail(last_report)