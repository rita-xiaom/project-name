from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#通过元素的id定位，表示方式为 #id值
driver.find_element_by_css_selector("#kw").send_keys("selenium")

#通过元素class定位，表示方式为 .class值
driver.find_element_by_css_selector(".s_ipt").send_keys("sele")

#通过元素属性值定位，表示方式为属性值
driver.find_element_by_css_selector("[autocomplete='off']").send_keys("python")
sleep(2)

driver.find_element_by_css_selector("#su").click()
sleep(3)

driver.get("http://www.51zxw.net")
#通过元素层级定位
driver.find_element_by_css_selector("form#loginFrom>div>div[2]>input").send_keys("python3")
sleep(2)

driver.quit()

