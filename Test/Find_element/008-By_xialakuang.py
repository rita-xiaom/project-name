from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Firefox()
driver.get("http:www.baidu.com")
driver.maximize_window()

above=driver.find_element_by_class_name("bri")
ActionChains(driver).move_to_element(above).perform()

sleep(2)
driver.find_element_by_name("tj_nuomi").click()
sleep(2)

driver.quit()


