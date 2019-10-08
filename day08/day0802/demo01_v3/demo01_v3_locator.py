#!/usr/bin/env python3
# coding=utf-8
from selenium.webdriver.common.by import By
class Page_Register_Locator:
    def __init__(self):
        #定位頁面元素信息
        self.findname=(By.XPATH,"//input[@name='username']")#實例變量前面必須加上self
        self.findpassword=(By.XPATH, "//input[@name='password']")
        self.findmail=(By.XPATH, "//input[@name='sex']")
        self.findfemail=(By.XPATH, "//input[@name='sex'][2]")
        self.findemail=(By.XPATH, "//input[@name='email']")
        self.findprofession=(By.XPATH,"//select[@name='profession']")
        self.findfilm=(By.XPATH,"//select[@name='findfilm']")
        self.findpainting=(By.XPATH, "//input[@name='painting']")
        self.findcomments=(By.XPATH, "//textarea")
        self.findsubmit=(By.XPATH, "//input[@name='submit']")