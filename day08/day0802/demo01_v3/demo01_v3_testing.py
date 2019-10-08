#!/usr/bin/env python3
# coding=utf-8
from selenium import webdriver
from day08.day0802.demo01_v3.demo01_v3_register import MyComments
import csv
from time import sleep
# 導入csv,處理csv格式文件
if __name__ == '__main__':
    # 打开页面
    # 测试数据1
    driver = webdriver.Chrome()
    # 打開頁面
    my_url=""
    test=MyComments(driver)
    test.open(my_url)
    # 測試數據（數據比較多）
    f=open('C:\Users\10845\PycharmProjects\myseleniumproject\day08\day0801/mydata2.csv','r')
    data=csv.reader(f)#二維列表
    # 測試數據1
    for mydata in data:#讀取每一行，放在mydata
        print(mydata)
        test.type_name(mydata[0])
        test.type_password(mydata[1])
        test.click_male()
        test.type_email(mydata[2])
        test.select_profession(mydata[3])
        test.click_film()
        test.click_painting()
        test.type_comments(mydata[4])
        sleep(1)
        test.click_submit()
        test.bye_bye()



