#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021-08-08 10:04
# @Author : Ya Ya.
# @QQ：276890663

from commen import ui02_method
from data import ui02_data

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)

#从字典中取出测试数据
url = ui02_data.data.get("url")
username = ui02_data.data.get("username")
password = ui02_data.data.get("password")
key = ui02_data.data.get("key")
print(url,username,password,key)

result = ui02_method.search_fun(driver=driver,url=url,username=username,password=password,key=key)
print(result)

if key in result:
    print("搜索成功！")
else:
    print("搜索失败！")