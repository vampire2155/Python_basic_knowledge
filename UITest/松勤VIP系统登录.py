# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/13 22:09

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('http://vip.ytesting.com/')
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element_by_id('userName').send_keys('K202005063504')
driver.find_element_by_id('password').send_keys('996969387')
#获取移动快的 元素
pollEle = driver.find_element_by_id('nc_1_n1z')
#使用ActionChains类 点击并保持住 移动快 元素,但是经过实践一次是无法把 移动快 移动到目的地的。
#首先移动 第一次 到 50px 的位置
ActionChains(driver).click_and_hold(on_element=pollEle).perform()
ActionChains(driver).move_to_element_with_offset(to_element=pollEle,xoffset=0,yoffset=50).perform()
sleep(0.5)
# 第二次 移动移动快 到 最后的位置
ActionChains(driver).move_to_element_with_offset(to_element=pollEle, xoffset=0, yoffset=114).perform()
driver.find_element_by_id('but_login').click()








