import unittest
from function import *
from BSTestRunner import BSTestRunner
import time

report_dir='./test_report'
test_dir='./test_case'
print("strat run test case")
discover=unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')


now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=report_dir+'/'+now+' result.html'
print("start write report......")

with open(report_name,'wb')as f:
    runner=BSTestRunner(stream=f,title='Test Report',description='login test report')
    runner.run(discover)
    f.close()

print("find latest report....")
latest_report=last_report(report_dir)

print("send email report....")
send_mail(latest_report)

print("Test End!")