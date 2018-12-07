from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")
driver.maximize_window()

js1="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js1)
sleep(2)

js2="var action=document.documentElement.scrollTop=0"
driver.execute_script(js2)
sleep(2)

driver.quit()