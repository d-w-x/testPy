# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:DW 
# date:2019/3/1
import json
from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://*")
with open("cookies.txt", "r") as fp:
    cookies = json.load(fp)
    for cookie in cookies:
        # cookie.pop('domain')
        driver.add_cookie(cookie)
driver.get("http://**")
sleep(8)
driver.close()
driver.quit()
