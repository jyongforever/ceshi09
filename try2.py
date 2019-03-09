# -*- coding:utf-8 -*-
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:63342/ceshi9/%E6%B3%A8%E5%86%8C%E5%AE%9E%E4%BE%8B.html?_ijt=bpjeil9m1jkn2labmstfao9d89")
dic1 = {"id":"userId","name":"testName"}
driver.add_cookie(cookie_dict=dic1)
cookies = driver.get_cookies()
print(cookies)
driver.quit()