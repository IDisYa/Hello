#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time : 2021-08-08 10:01
# @Author : Ya Ya.
# @QQ：276890663

import time

#打开网页函数
def open_page(driver,url):
    driver.get(url)
    driver.maximize_window()

#登录函数
def login_fun(driver,username,password):
    driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
    driver.find_element_by_xpath("//input[@id='password']").send_keys("123456")
    driver.find_element_by_xpath("//div[@class='form-group']//button").click()

#搜索函数
def search_fun(driver,url,username,password,key):
    open_page(driver,url)
    login_fun(driver,username,password)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    id_iframe = id+"-frame"
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(id_iframe)))
    driver.find_element_by_xpath("//input[@id='searchNumber']").send_keys(key)
    driver.find_element_by_xpath("//span[text()='查询']").click()
    time.sleep(1)
    result = driver.find_element_by_xpath("//div[contains(text(),'448')]").text
    return result