#!/usr/bin/env python3
# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

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
