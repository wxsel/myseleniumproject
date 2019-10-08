#!/usr/bin/env python3
# coding=utf-8
#!/usr/bin/env python3
# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class MyComments:
    #定位頁面元素信息
    findname=(By.XPATH,"//input[@name='username']")
    findpassword=(By.XPATH, "//input[@name='password']")
    findmail=(By.XPATH, "//input[@name='sex']")
    findfemail=(By.XPATH, "//input[@name='sex'][2]")
    findemail=(By.XPATH, "//input[@name='email']")
    findprofession=(By.XPATH,"//select[@name='profession']")
    findfilm=(By.XPATH,"//select[@name='findfilm']")
    findpainting=(By.XPATH, "//input[@name='painting']")
    findcomments=(By.XPATH, "//textarea")
    findsubmit=(By.XPATH, "//input[@name='submit']")

    # 構造函數
    def __init__(self,driver):#driver局部變量，在函數體中使用
        self.driver=driver
    # 打开浏览器
    # self定義時一定要有
    def open(self,url):
        base_url=url
        self.driver.get(base_url)
    # 输入姓名
    def type_name(self,n):
        self.name = self.driver.find_element(*self.findname)#實例變量,可變長
        self.name.send_keys(n)
    # 输入密码
    def type_password(self,p):
        self.password = self.driver.find_element(*self.findpassword)
        self.password.send_keys(p)
    # 点击性别男
    def click_male(self):
        self.male = self.driver.find_element(*self.findmail)
        self.male.click()
    # 点击性别女
    def click_female(self):
        self.female = self.driver.find_element(*self.findfemail)
        self.female.click()
    # 输入邮箱
    def type_email(self,e):
        self.email = self.driver.find_element(*self.findmail)
        self.email.send_keys(e)
    # 选择专业
    # 形参是个局部变量
    def select_profession(self,t):
        self.profession = self.driver.find_element(*self.findprofession)
        self.p1 = Select(self.profession)
        self.p1.select_by_visible_text(t)
    # 点击影视娱乐
    def click_film(self):
        self.film = self.driver.find_element(*self.findfilm)
        if self.film.is_selected() == False:
            self.film.click()
    # 点击绘画书法
    def click_painting(self):
        self.painting = self.driver.find_element(*self.findpainting)
        if self.painting.is_selected() == False:
            self.painting.click()
    # 输入留言
    def type_comments(self,c):
        self.comments = self.driver.find_element(*self.findcomments)
        self.comments.send_keys(c)
    # 点击提交
    def click_submit(self):
        self.submit = self.driver.find_element(*self.findsubmit)
        self.submit.click()
    def bye_bye(self):
        self.driver.quit()