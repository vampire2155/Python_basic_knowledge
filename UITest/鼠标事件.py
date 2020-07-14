# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/14 10:01

from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://www.baidu.com/')
driver.maximize_window()

moreEle = driver.find_element_by_name('tj_briicon')
#对定位到的元素执行鼠标悬停的操作  move_to_element() 只是把鼠标移动到元素的中间   perform()是执行 悬停这个操作
ActionChains(driver).move_to_element(moreEle).perform()
sleep(1)

QRcode = driver.find_element_by_css_selector('img.icon')
ActionChains(driver).move_to_element(QRcode).perform()

#鼠标右键操作 事件
ActionChains(driver).context_click(moreEle).perform()

#鼠标双击操作
ActionChains(driver).double_click()

#拖动元素 事件
ActionChains(driver).drag_and_drop(moreEle, QRcode).perform()  #这里因为没有合适的界面可以操作，所以随便传递了两个实参。
#对函数 drag_and_drop的解释：
# Holds down the left mouse button on the source element,
# then moves to the target element and releases the mouse button.

#移动某个元素到  某个位置
# ActionChains(driver).drag_and_drop_by_offset(source, xoffset, yoffset).perform()


driver.quit()




