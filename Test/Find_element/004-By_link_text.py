from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

driver.find_element_by_link_text("程序开发").click()
sleep(2)
driver.maximize_window()
driver.find_element_by_link_text("Python").click()
sleep(2)

# driver.find_element_by_class_name("courses").click()
# sleep(3)
driver.find_element_by_xpath("/html/body/div[2]/div[5]/div[5]/a[1]/div[2]").click()
sleep(2)
driver.find_element_by_partial_link_text("神秘面纱").click()
sleep(2)

driver.quit()