from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Chrome()
time.sleep(1)
browser.get('http://www.qmzs.com/categroy')
assert "全民助手" in browser.title
ele = browser.find_element_by_name("searchInput")
ele.clear()
ele.send_keys("部落冲突")
ele.send_keys(Keys.ENTER)
print("开始搜")
time.sleep(1)
btn = browser.find_element_by_id("ss_searchBtn")
btn.click()
time.sleep(1)
#browser.close()
