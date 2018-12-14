import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('www.baidu.com')
time.sleep(2)
driver.quit()
# dlks