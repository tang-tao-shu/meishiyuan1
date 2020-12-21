# -*- coding: utf-8 -*-
# @Time : 2020/12/19 15:57
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : mytest.py
# @Project : meishiyuan
import unittest
from appium import webdriver
import test1
class MyTset(unittest.TestCase):
    """测试用例基类"""
    def setUp(self) -> None:
        pass
    def test_yonlisan(self):
        self.test1

    def tearDown(self) -> None:
        self.driver.quit()








