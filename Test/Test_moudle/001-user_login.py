from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/")

#登陆帝国网站
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("51zxw")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")

#点击登陆
driver.find_element_by_name("Submit").click()
sleep(8)

#退出登陆
driver.find_element_by_link_text("退出").click()
driver.switch_to_alert().accept()
sleep(3)

driver.quit()