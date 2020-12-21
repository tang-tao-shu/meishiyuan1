# -*- coding: utf-8 -*-
# @Time : 2020/12/19 10:17
# @Author : 唐涛
# @Email : 2410725336@qq.com
# @File : test1.py
# @Project : meishiyuan
from appium import webdriver
from time import sleep
from model.app_driver import app_driver
desired_capabilities = {'platformName': 'Android',
                         'deviceName': 'emulator-5554',
                         'platformVersion': '7.1.2',
                         'appPackage': 'com.meishio.app',
                         'unicodekeyboard': True,
                         'resetkeyboard': True,
                         'appActivity': 'module.home.activity.SplashActivity'
                         }

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities)
driver.implicitly_wait(30)
# 点击跳过
driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.meishio.app:id/lead_skip\"]").click()
sleep(3)
# 点击我的
driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[4]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
sleep(3)
# 点击登录/注册
driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.meishio.app:id/user_name\"]").click()
sleep(3)
# 登录
driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_username_email_phone\"]").send_keys("junmoxiao")
driver.find_element_by_xpath("//android.widget.EditText[@resource-id=\"com.meishio.app:id/user_login_password\"]").send_keys("zj697366")
driver.find_element_by_xpath("//android.widget.Button[@resource-id=\"com.meishio.app:id/user_login_btn\"]").click()
sleep(3)
# 点击首页
driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
sleep(2)
# 刷新
driver.swipe(544,795,628,1670,500)
sleep(3)
# 点击农村草鸡蛋
driver.find_element_by_xpath("//android.widget.GridView[@resource-id=\"com.meishio.app:id/product_recommend_home_gridview\"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]").click()
sleep(3)
# 点击加入购入车
driver.tap([(420,1879)],500)
# 点击确认
driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.meishio.app:id/product_properties_done\"]").click()
sleep(3)
# 点击返回
driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.meishio.app:id/goods_detail_head_tab_return_img\"]").click()
# 点击购物车
driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[3]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]").click()
# 点击商品
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.meishio.app:id/shop_cart_item_choice\"]').click()
sleep(3)
# 点击结算
driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/shop_cart_view_balance\"]').click()
sleep(3)
# 选择配送方式
driver.find_element_by_xpath("//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_shipping_type\"]").click()
sleep(3)
# 点击中通速递
driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.meishio.app:id/shipping_item_check\"]").click()
sleep(3)
# 点击发票内容
driver.find_element_by_xpath('//android.widget.TextView[@resource-id=\"com.meishio.app:id/order_confirm_invoice_type\"]').click()
sleep(3)
# 点击不要发票
driver.tap([(80,984)],500)
# 点击确认
driver.tap([(990,128)],500)
# 点击留言
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]').click()
sleep(3)
# 点击提交订单
driver.find_element_by_xpath("//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]").click()
sleep(3)
# 点击返回
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]').click()
sleep(3)
# 点击返回
driver.find_element_by_xpath('//android.widget.ImageView[@resource-id=\"com.meishio.app:id/user_top_view_back\"]').click()
sleep(3)
# 点击主页
driver.find_element_by_xpath('//android.widget.LinearLayout[@resource-id=\"com.meishio.app:id/main_tool_bg\"]/android.widget.LinearLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]').click()
sleep(3)
# 点击订单
driver.quit()


