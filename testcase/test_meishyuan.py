# -*- coding: utf-8 -*-
# @Time : 2020/12/19 21:28
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : test_meishyuan.py
# @Project : 三阶段项目2
from time import sleep
from page.Base_Page import BasePage
from page.my_page import MyPage
from page.login_page import LoginPage
from page.shopping_car_page import CarPage
from model.app_driver import app_driver
import unittest
class MyTest_meishiyuan(app_driver()):
    '''测试美食园'''
    def setUp(self):
        self.driver=app_driver()
    def test_a(self):
        '''测试用例a'''
        # LoginPage(self.driver).login
        pass
    def test_b(self):
        pass

if __name__ == '__main__':
    unittest.main()






