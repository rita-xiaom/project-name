from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_link_text("设置").click()
driver.find_element_by_link_text("搜索设置").click()
sleep(2)

driver.find_element_by_css_selector(".prefpanelgo").click()

#引入弹窗警告信息
alert=driver.switch_to_alert()
alert.accept()

sleep(2)
driver.quit()