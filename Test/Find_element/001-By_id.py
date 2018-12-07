from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_name("wd").send_keys("selenium2")
sleep(2)

driver.find_element_by_id("su").click()
sleep(2)

driver.quit()