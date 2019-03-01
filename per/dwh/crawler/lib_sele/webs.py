# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:DW 
# date:2019/2/28
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
# driver.get("http://*")
# inputs = driver.find_element(By.NAME, "username")
# inputs.send_keys("*")
# inputs = driver.find_element(By.NAME, "password")
# inputs.send_keys("*")
# button = driver.find_element_by_id("loginbtn")
# button.click()
# cookies = driver.get_cookies()
# print(cookies)
# with open("cookies.txt", "w+") as fp:
#     json.dump(cookies, fp)

# driver.get("https://github.com")
# ins = driver.find_element_by_id("user_email")
# ins.send_keys("112")

# driver.get("https://github.com")
# try:
#     ins = WebDriverWait(driver, 5).until(lambda drivers: drivers.find_element_by_name("user_email"))
# finally:
#     driver.quit()
driver.get("http://baidu.com")
driver.execute_script("window.open('https://baidu.com')")
driver.switch_to.window(driver.window_handles[0])
sleep(8)
driver.close()
driver.quit()
