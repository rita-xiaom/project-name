from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

#定位搜索框
driver.find_element_by_css_selector("#kw").clear()
driver.find_element_by_css_selector("#kw").send_keys("python")

sleep(2)
#键盘操作，全选
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'a')
#键盘操作，复制或者剪切
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'c')
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,'x')

sleep(2)
#打开搜狗浏览器
driver.get("http://www.sogou.com")
#定位搜索框
driver.find_element_by_css_selector(".sec-input").clear()
driver.find_element_by_css_selector(".sec-input").send_keys(Keys.CONTROL,'v')
driver.find_element_by_css_selector("#stb").click()

sleep(3)
driver.quit()