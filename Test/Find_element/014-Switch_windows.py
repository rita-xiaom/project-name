from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()


#打开第一个窗口，并且获取当前页面句柄
driver.get("https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=9621b46f00028d1a&rsv_t=ff41apjan7pjeyOkMaeT%2BUR0qZ6bj%2FufoLQoUsdtHi8udx9XaoKlI2xGQYE&rqlang=cn&rsv_enter=1&rsv_sug3=7&rsv_sug1=6&rsv_sug7=100&rsv_sug2=0&inputT=2221&rsv_sug4=4288")
selenium_index=driver.current_window_handle
sleep(2)

#打开第二个页面
driver.find_element_by_partial_link_text("廖雪峰").click()
sleep(4)

#回到第一个页面，打开第三个页面
driver.switch_to_window(selenium_index)
sleep(4)
driver.find_element_by_link_text("Welcome to Python.org").click()
sleep(4)
driver.quit()