from LoginClass_poro import *
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost/")
driver.maximize_window()
driver.implicitly_wait(10)

Login().user_login(driver,'51zxw','123456')
sleep(3)
Login().user_loginout(driver)
sleep(3)


Login().user_login(driver,'51zxwpro','123456')
sleep(2)
Login().user_loginout(driver)
sleep(3)

driver.quit()