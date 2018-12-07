from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()

driver.find_element_by_css_selector(".soutu-btn").click()
driver.find_element_by_css_selector(".upload-pic").send_keys(r"F:\Game\d14.jpg")
sleep(2)

driver.quit()