# -*- coding: utf-8 -*-
# @Time : 2020/12/19 20:28
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : Base_Page.py
# @Project : 三阶段项目2
class BasePage():
    '''页面类基类'''
    def __init__(self,driver):
        self.driver=driver

    def find_element(self,loc):
        return self.driver.find_element(*loc)


