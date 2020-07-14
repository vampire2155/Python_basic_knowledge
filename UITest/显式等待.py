# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/10 20:55
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from win32com import client
from time import sleep

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://tinypng.com/')
driver.maximize_window()

#显式等待 语句比较长，可以把它封装成一个函数，方便执行元素定位时调用
def wait(driver,timeout,poll_frequency,byMethod,element):
    '''
    :param driver: driver
    :param timeout: 等待的超时时间
    :param poll_frequency: 默认的轮询时间是 0.5秒
    :param byMethod: 定位的方法
    :param element: 元素
    :return:  返回找到的元素对象，这里必须写返回值，否则，返回为None，是没有任何方法的。
    '''
    ele = WebDriverWait(driver,timeout,poll_frequency).until(EC.visibility_of_element_located(
        (byMethod,element)
        )
    )
    return ele

ele = wait(driver,2,0.5,By.CSS_SELECTOR,'figure.icon')
ele.click()
sh = client.Dispatch('WScript.shell')
file = "G:\Python_scripts\\UITest\\a.png\n"
sleep(2)  #这里一定要等待一下，否则代码执行太快，来不及输入。
sh.Sendkeys(file)
driver.quit()

WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, 'kw')))    #元组传参


WebDriverWait(driver, 10, 0.5).until(EC.visibility_of_element_located((By.ID, 'kw')))





