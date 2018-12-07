from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://authtest.zjmiec.cn/pages/login.html")

driver.find_element_by_name(u'userName').clear()
driver.find_element_by_name(u'userName').send_keys("dr_dengzm") #用户名

driver.find_element_by_name(u'passWord').clear()
driver.find_element_by_name(u'passWord').send_keys('123456') #密码

driver.find_element_by_name(u'rdm').clear()
driver.find_element_by_name(u'rdm').send_keys('0000') #验证码

driver.find_element_by_class_name(u'submit_btn').click() #点击登录
driver.maximize_window()
sleep(3)

driver.find_element_by_xpath("//*[@sysid='b80cdca80000000a']").click()
driver.maximize_window()
sleep(3)
