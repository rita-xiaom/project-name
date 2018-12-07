from selenium import webdriver
from selenium.common.exceptions import NoSuchAttributeException
from time import sleep,ctime

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
sleep(2)

#设置等待时间为5s
driver.implicitly_wait(5)

print(ctime())
try:
    driver.find_element_by_css_selector("#kw").send_keys("python")
    driver.find_element_by_css_selector("#su").click()
except NoSuchAttributeException as msg:
    print(msg)
finally:
    print(ctime())

sleep(2)
driver.quit()


