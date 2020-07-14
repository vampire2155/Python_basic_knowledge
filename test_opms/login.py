# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/13 23:44
import time
from selenium import webdriver

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
class Login_class():
    def login(self):
        # 方法二：通过import globalparam.py 获取
        driver.get('http://127.0.0.1:8088/')
        driver.maximize_window()
        #输入用户名，用户名username是 从 globalparam.py 获取
        driver.find_element_by_name('username').send_keys('libai')
        # driver.find_element_by_xpath('//*[@id="login-form"]/div[2]/input[1]').send_keys('libai')
        #输入密码，password 从 globalparam.py 获取
        driver.find_element_by_name('password').send_keys('opmsopms123')
        #点击登录按钮
        driver.find_element_by_class_name('btn-login').click()
        #因为登录完成以后会弹出一个登录成功的提示框，等待3s后会自动消失，所以，这里强制等待3.5s秒钟
        time.sleep(3.5)



