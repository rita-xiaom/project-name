import unittest
from HTMLTestRunner import HTMLTestRunner
import time

test_dir='./test_case'
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
if __name__ == '__main__':
    report_dir='./test_report'
    now=time.strftime("%Y-%m-%d %H-%M-%S")
    report_name=report_dir+'/'+now+' result.html'

    with open(report_name,'wb')as f:
        runner=HTMLTestRunner(stream=f,title="Test Report",description='test  case result')
        runner.run(discovery)
    f.close()