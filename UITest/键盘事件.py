# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/14 10:33

from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.implicitly_wait(2)
driver.get('https://www.baidu.com/')

searchEle = driver.find_element_by_id('kw')
searchEle.send_keys('selenium')

#全选操作  即 ctrl + a  操作
searchEle.send_keys(Keys.CONTROL, 'a')
sleep(3)
#复制操作  即ctrl + c  操作
searchEle.send_keys(Keys.CONTROL, 'c')
sleep(3)
# BackSpace操作  即键盘上的 BackSpace操作
searchEle.send_keys(Keys.BACK_SPACE)      #  Keys.BACKSPACE == Keys.BACK_SPACE
# searchEle.send_keys(Keys.BACKSPACE)
sleep(3)

searchEle.send_keys(Keys.CONTROL, 'a')
sleep(3)

#粘贴 操作  即ctrl + v  操作
searchEle.send_keys(Keys.CONTROL, 'v')
sleep(3)
#空格 操作  即敲击 键盘上的 空格键
searchEle.send_keys(Keys.SPACE)
sleep(3)

#回车键  Enter
searchEle.send_keys(Keys.ENTER)

driver.quit()

