from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

driver.add_cookie({'name':'BAIDUID','value':'D9763C55A3958FD8D5D8BAC427AB50EE:SL=0:NR=10:FG=1'})
driver.add_cookie({'name':'BDUSS','value':'kp6TTJsNy1aUUdpb1BIb0tJMU9pcDkzamNaLXo2UkpIY1cyTld0eEJlZEwzQWRjQUFBQUFBJCQAAAAAAAAAAAEAAABOGcslsru2~sfgtLrRp9SwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEtP4FtLT-BbZ'})
sleep(3)

driver.refresh()
sleep(3)
driver.quit()