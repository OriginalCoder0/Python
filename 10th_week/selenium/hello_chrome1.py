from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 获取百度一下输入框
input = driver.find_element_by_id("kw")
# 搜索python信息
input.send_keys("python")
# 回车
input.send_keys(Keys.ENTER)


print(driver.page_source)

# 关闭
#driver.close()