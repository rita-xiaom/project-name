from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()

driver.get_screenshot_as_file(r"F:\Game\51zxw.jpg")
sleep(2)

driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r"F:\Game\baidu.jpg")
sleep(2)

driver.quit()