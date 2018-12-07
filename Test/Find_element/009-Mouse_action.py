from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
#定义driver
driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.maximize_window()

#鼠标双击操作
driver.find_element_by_css_selector("#kw").send_keys("python")
element=driver.find_element_by_css_selector("#kw")
sleep(2)
ActionChains(driver).double_click(element).perform()
sleep(2)
#鼠标右键操作
ActionChains(driver).context_click(element).perform()
sleep(2)
#鼠标悬停
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()
sleep(2)
#页面跳转
# driver.find_element_by_css_selector(".setpref").click()
# sleep(2)
driver.find_element_by_link_text("高级搜索").click()
sleep(2)
driver.quit()
