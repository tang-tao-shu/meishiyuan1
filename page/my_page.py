# -*- coding: utf-8 -*-
# @Time : 2020/12/19 19:29
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : my_page.py
# @Project : 三阶段项目2
from appium.webdriver.common.mobileby import By
from page.Base_Page import BasePage
class MyPage(BasePage):
    '''首页页面'''
    '''定位器'''
    shouye_locator=(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    jidan_locator=(By.XPATH,'//android.widget.GridView[@resource-id=\"com.meishio.app:id/product_recommend_home_gridview\"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]')
    queren_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/product_properties_done\"]')
    fanhui_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/goods_detail_head_tab_return_img\"]')

    def click_shouye(self):  #点击首页
        self.find_element(self.shouye_locator).click()

    def click_jidan(self): #点击鸡蛋
        self.find_element(self.jidan_locator).click()

    def click_queren(self):#点击确认
        self.find_element(self.queren_locator).click()

    def click_fanhui(self):#点击返回
        self.find_element(self.fanhui_locator).click()

    def suanxing(self):
        self.driver.swipe(544,795,628,1670,500)

    def gouwuche(self):
        self.driver.tap([(420,1879)],500)


    def myzhuye(self):
        self.click_shouye()
        self.suanxing()
        self.click_jidan()
        self.gouwuche()
        self.click_queren()
        self.click_fanhui()

