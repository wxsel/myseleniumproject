#!/usr/bin/env python3
# coding=utf-8
from day08.day0802.demo01_v3.demo01_v3_locator import Page_Register_Locator
from selenium.webdriver.support.select import Select
from day08.day0802.demo01_v3.demo01_v3_mypage import MyPage
class MyComments(MyPage):#子類繼承父類
    # 構造函數
    def __init__(self,driver):#driver局部變量，在函數體中使用
        MyPage.__init__(self,driver)#子類調用父類,調用父類的構造函數來完成初始化
        self.Lr=Page_Register_Locator()#實例化，self是一個全局變量

    # 输入姓名
    def type_name(self,n):
        self.name = self.driver.find_element(*self.Lr.findname)#實例變量,可變長
        self.name.send_keys(n)
    # 输入密码
    def type_password(self,p):
        self.password = self.driver.find_element(*self.Lr.findpassword)
        self.password.send_keys(p)
    # 点击性别男
    def click_male(self):
        self.male = self.driver.find_element(*self.Lr.findmail)
        self.male.click()
    # 点击性别女
    def click_female(self):
        self.female = self.driver.find_element(*self.Lr.findfemail)
        self.female.click()
    # 输入邮箱
    def type_email(self,e):
        self.email = self.driver.find_element(*self.Lr.findemail)
        self.email.send_keys(e)
    # 选择专业
    # 形参是个局部变量
    def select_profession(self,t):
        self.profession = self.driver.find_element(*self.Lr.findprofession)
        self.p1 = Select(self.profession)
        self.p1.select_by_visible_text(t)
    # 点击影视娱乐
    def click_film(self):
        self.film = self.driver.find_element(*self.Lr.findfilm)
        if self.film.is_selected() == False:
            self.film.click()
    # 点击绘画书法
    def click_painting(self):
        self.painting = self.driver.find_element(*self.Lr.findpainting)
        if self.painting.is_selected() == False:
            self.painting.click()
    # 输入留言
    def type_comments(self,c):
        self.comments = self.driver.find_element(*self.Lr.findcomments)
        self.comments.send_keys(c)
    # 点击提交
    def click_submit(self):
        self.submit = self.driver.find_element(*self.Lr.findsubmit)
        self.submit.click()
