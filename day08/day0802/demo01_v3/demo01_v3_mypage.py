#!/usr/bin/env python3
# coding=utf-8
class MyPage:
    # 構造函數
    def __init__(self, driver):  # driver局部變量，在函數體中使用
        self.driver = driver
    # 打开浏览器
    # self定義時一定要有
    def open(self, url):
        base_url = url
        self.driver.get(base_url)
    def bye_bye(self):
        self.driver.quit()