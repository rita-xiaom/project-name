from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
file_path=r'E:\Destination Folder\pycharm\Test\Find_element\frame.html'
driver.get(file_path)

#切换frame嵌套页面
driver.switch_to.frame("search")

#页面元素的定位
driver.find_element_by_css_selector(".sec-input").send_keys("python")
driver.find_element_by_css_selector("#stb").click()

sleep(2)
driver.quit()