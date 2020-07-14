# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/13 21:45

from selenium import webdriver

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://www.baidu.com/')
driver.maximize_window()
driver.find_element_by_css_selector('.title-text.c-font-medium.c-color-t').click()

#获取所有的标签页的句柄
all_handles = driver.window_handles
# 使用for循环进行判断
for handle in all_handles:
    driver.switch_to.window(handle)
    if handle.title() == '百度搜索风云榜':  #当切换到这个标签页时如果标题与预期的标题一致，则结束循环。
        break

#然后点击这个标签 页的小说 按钮
driver.find_element_by_css_selector('#main-nav > li:nth-child(3) >a').click()
driver.quit()







