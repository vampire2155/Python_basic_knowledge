from selenium import webdriver
import time
driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get('https://www.baidu.com/')
driver.maximize_window()
time.sleep(1)
#截取 整个页面 的图片
driver.get_screenshot_as_file('./a.png')
driver.window.scro




# driver.quit()
