# -*- coding: utf-8 -*-
# @Time : 2020/12/19 16:24
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : login_page.py
# @Project : 三阶段项目2
from appium.webdriver.common.mobileby import By
from model.app_driver import app_driver
from page.Base_Page import BasePage

class LoginPage(BasePage):
    """登录页面类"""
    """定位器"""
    tiaoguo_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/lead_skip\"]')
    my_locator = (By.XPATH,'//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]')
    denglukuang_locator=(By.XPATH,'//android.widget.TextView[@resource-id=\"com.meishio.app:id/user_name\"]')

    username_locator=(By.ID,'com.meishio.app:id/user_login_username_email_phone')
    password_locator=(By.ID,'com.meishio.app:id/user_login_password')
    login_locator=("//android.widget.Button[@resource-id=\"com.meishio.app:id/user_login_btn\"]")
    def click_tiaoguo(self):#点击跳过
        self.find_element(self.tiaoguo_locator).click()

    def click_my(self):#点击【我的】
        self.find_element(self.my_locator).click()

    def click_denglukuang(self):#点击登录/注册
        self.find_element(self.denglukuang_locator).click()

    def login_uesrname(self):#输入用户名
        '''用户名输入框'''
        self.driver.find_element(self.username_locator).send.keys("junmoxiao")

    def login_password(self):#输入密码
        '''密码输入框'''
        self.driver.find_element(self.password_locator).send_keys('zj697366')

    def login_denglu(self):#点击登录
        '''登录按钮'''
        self.driver.find_element(self.login_locator).click()

    def login(self):
        '''登录操作'''
        self.click_tiaoguo()
        self.click_my()
        self.click_denglukuang()
        self.login_uesrname()
        self.login_password()
        self.login_denglu()


