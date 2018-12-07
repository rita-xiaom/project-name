from LoginPage import *
from selenium import webdriver

driver=webdriver.Firefox()

username='51zxw'
password='123456'

test_uesr_login(driver,username,password)
sleep(3)
driver.quit()