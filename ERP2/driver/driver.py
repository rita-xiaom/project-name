from selenium import webdriver

#启动浏览器驱动
def  browser():
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # driver = webdriver.Ie()

    driver.get("http://www.baidu.com")
    return driver

#调试运行
if __name__ == '__main__':
    browser()