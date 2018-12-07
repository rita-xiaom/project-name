from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("selenium")
# driver.find_element_by_xpath("//input[@id='kw']").send_keys("python")
# driver.find_element_by_xpath("//input[@name='wd']").send_keys("python")
driver.find_element_by_xpath("//input[@class='s_ipt']").send_keys("python")
sleep(2)

driver.find_element_by_id("su").click()
sleep(2)

driver.quit()