# -*- coding: utf-8 -*-
# @Time : 2020/12/19 19:29
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : shopping_car_page.py
# @Project : 三阶段项目2
from appium.webdriver.common.mobileby import By
from page.Base_Page import BasePage
class CarPage(BasePage):
    '''购物车页面'''
    '''定位器'''
    gouwuche_loactor=(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    shangping_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/shop_cart_item_choice\"]')
    jiesuan_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/shop_cart_view_balance\"]')
    peisong_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_shipping_type\"]')
    zhongtong_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/shipping_item_check\"]')
    fapiaoneiron_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_invoice_type\"]')
    liuyan_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]')
    dingdan_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]')
    fanhui_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]')
    fanhuihui_locator=(By.XPATH,'//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]')
    diandingdan_locator=(By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')

    def click_gouwuche(self):#点击购物车
        self.find_element(self.gouwuche_loactor).click()

    def click_shangping(self):#点击商品
        self.find_element(self.shangping_locator).click()

    def click_jiesuan(self):#点击结算
        self.find_element(self.jiesuan_locator).click()

    def click_peisong(self):#点击配送
        self.find_element(self.peisong_locator).click()

    def click_zhongtong(self):#点击中通
        self.find_element(self.zhongtong_locator).click()

    def click_fapiaoneiron(self):#点击发票内容
        self.find_element(self.fapiaoneiron_locator).click()

    def fapiao(self):#点击不要发票
        self.driver.tap([(80,984)],500)

    def queren(self):#点击确认
        self.driver.tap([(990,128)],500)

    def click_liuyan(self):
        self.find_element(self.liuyan_locator).click()

    def click_dingdan(self):
        self.find_element(self.dingdan_locator).click()

    def click_fanhui(self):
        self.find_element(self.fanhuihui_locator).click()

    def click_fanhuihui(self):
        self.find_element(self.fanhuihui_locator).click()

    def click_diandingdan(self):
        self.find_element(self.diandingdan_locator).click()

    def gouwuche(self):
        self.click_gouwuche()
        self.click_shangping()
        self.click_jiesuan()
        self.click_peisong()
        self.click_zhongtong()
        self.click_fapiaoneiron()
        self.fapiao()
        self.queren()
        self.click_liuyan()
        self.click_dingdan()
        self.click_fanhui()
        self.click_fanhuihui()
        self.click_diandingdan()



