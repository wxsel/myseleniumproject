#!/usr/bin/env python3
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver=webdriver.Chrome()
base_url=""
driver.get(base_url)
# 测试用例
name.send_keys("张晓明")
password.send_keys("123456")
male.click()
email.send_keys('xiaoming@126.com')
p1=Select(profession)
p1.select_by_visible_text("法律相关")
if film.is_selected()==False:
    film.click()
if painting.is_selected()==False:
    painting.click()
comments.send_keys("软件测试工程师")
sleep(1)
submit.click()
driver.quit()