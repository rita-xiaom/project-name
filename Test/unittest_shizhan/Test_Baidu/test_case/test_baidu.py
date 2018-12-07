from selenium import webdriver
from time import sleep
import unittest

class TestBaidu(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Firefox()
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.baidu.com")

    def testbaidu(self):
        driver=self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("Selenium 自学网")
        driver.find_element_by_id("su").click()
        sleep(2)

        title=driver.title
        self.assertEqual(title,"Selenium 自学网_百度搜索")
        sleep(3)
        driver.find_element_by_partial_link_text("Selenium自动化").click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()