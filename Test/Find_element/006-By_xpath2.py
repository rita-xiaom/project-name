from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/login?redirect_url=http%3A%2F%2Fwww.51zxw.net%2F")

sleep(3)
driver.maximize_window()

# driver.find_element_by_xpath("//form[@id='loginFrom'/div/div[2]/input[type='text']").send_keys('selenium')
driver.find_element_by_xpath("//input[@id='loginStr']").send_keys("selenium")
sleep(3)

#一直报错，SytRealError：表达式不是合法表达式，后续研究
# driver.find_element_by_xpath("//form[@id='loginFrom'/div/div[4]/input[type='password']"").send_keys('123456')
driver.find_element_by_xpath("//*[@id='pwd']").send_keys("123456")
sleep(3)

driver.find_element_by_link_text("登录").click()
sleep(2)

driver.quit()
