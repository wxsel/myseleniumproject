#!/usr/bin/env python3
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class MyComments():
    # 打开浏览器
    # self定義時一定要有
    def open(self,url):
        base_url=url
        driver.get(base_url)
    # 输入姓名
    def type_name(self,n):
        name = driver.find_element(By.XPATH, "//input[@name='username']")
        name.send_keys(n)
    # 输入密码
    def type_password(self,p):
        password = driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(p)
    # 点击性别男
    def click_male(self):
        male = driver.find_element(By.XPATH, "//input[@name='sex']")
        male.click()
    # 点击性别女
    def click_female(self):
        female = driver.find_element(By.XPATH, "//input[@name='sex'][2]")
        female.click()
    # 输入邮箱
    def type_email(self,e):
        email = driver.find_element(By.XPATH, "//input[@name='email']")
        email.send_keys(e)
    # 选择专业
    # 形参是个局部变量
    def select_profession(self,t):
        profession = driver.find_element(By.XPATH, "//select[@name='profession']")
        p1 = Select(profession)
        p1.select_by_visible_text(t)
    # 点击影视娱乐
    def click_film(self):
        film = driver.find_element(By.XPATH, "//input[@name='film']")
        if film.is_selected() == False:
            film.click()
    # 点击绘画书法
    def click_painting(self):
        painting = driver.find_element(By.XPATH, "//input[@name='painting']")
        if painting.is_selected() == False:
            painting.click()
    # 输入留言
    def type_comments(self,c):
        comments = driver.find_element(By.XPATH, "//textarea")
        comments.send_keys(c)
    # 点击提交
    def click_submit(self):
        submit = driver.find_element(By.XPATH, "//input[@name='submit']")
        submit.click()
    def bye_bye(self):
        driver.quit()

if __name__ == '__main__':
    # 打开页面
    # 测试数据1
    driver = webdriver.Chrome()
    # 打開頁面
    my_url=""
    test=MyComments()
    test.open(my_url)
    # 測試數據1
    mydata = {"姓名": "张晓明", "密码": "123456", "邮箱": "xiaoming@126.com", "专业": "法律相关", "留言": "软件测试工程师"}
    mydata = {"姓名": "Tom", "密码": "abcdef", "邮箱": "Tom@126.com", "专业": "藝術/設計", "留言": "selenium"}
    myname=["張三","王小明","黎明"]
    mypassword=["123456","abcdef","xyz"]
    mymail=["xiaoming@126.com","Tom@126.com","liming@tedu.cn"]
    myprofession=["法律相關","藝術/設計","教育/研究"]
    mycomments=["你好","軟件測試工程師","selenium"]
    for name,password,email,profession,comments in zip(myname,mypassword,mymail,myprofession,mycomments):
        # test.type_name(mydata["姓名"])
        test.type_name(name)
        test.type_password(password)
        test.click_male()
        test.type_email(email)
        test.select_profession(profession)
        test.click_film()
        test.click_painting()
        sleep(1)
        # type_comments("留言")
        test.click_submit()

# 測試數據2

    test.type_name(mydata["姓名"])
    test.type_password(mydata["密码"])
    test.click_female()
    test.type_email(mydata["邮箱"])
    test.select_profession("专业")
    # click_film()
    test.click_painting()
    sleep(1)
    # type_comments("留言")
    test.click_submit()
    test.bye_bye()



