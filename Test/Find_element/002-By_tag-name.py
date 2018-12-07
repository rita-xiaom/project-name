from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/login")

driver.find_element_by_class_name("checked").click()
sleep(2)
driver.find_elements_by_tag_name("input")[0].send_keys("selenium")
sleep(3)

# driver.quit()

#定位异常，后续研究