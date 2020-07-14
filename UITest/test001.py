from selenium import webdriver
import time,pytest

driver = webdriver.Chrome(r'G:\Selenium_java\chromedriver.exe')
driver.get(r'G:\Python_scripts\UITest\test.html')
driver.maximize_window()
#找到这个框架
iframe = driver.find_element_by_id('iframe1')
#切换到框架里面
driver.switch_to.frame(iframe)
driver.find_element_by_link_text('高考加油').click()   #点击高考加油
#获取句柄
handles = driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)          #切换到这个句柄
    if '高考_百度搜索' in driver.title:        #如果这个句柄的标题条件成立，则结束循环
        break
time.sleep(1)
driver.find_element_by_class_name('search_tool').click()  #点击搜索工具
#点击  时间不限
driver.find_element_by_css_selector("#container > div.head_nums_cont_outer.OP_LOG > div > div.search_tool_conter > span.search_tool_tf").click()
#点击  自定义  下面的开始时间
dateSelector = driver.find_element_by_css_selector("#c-tips-container > div:nth-child(1) > div > div > ul > li.c-tip-custom > p.c-tip-custom-st > input")
dateSelector.click()
#在弹出来的日期选择框中，选择一个非当天的日期
#要实现上面的操作，可以通过先把当前日期删除掉，然后重新赋值
dateSelector.clear()
#输入开始日期
dateSelector.send_keys('2020-07-01')

#选择结束日期
endDate = driver.find_element_by_css_selector('#c-tips-container > div:nth-child(1) > div > div > ul > li.c-tip-custom > p.c-tip-custom-et > input')
endDate.click()
endDate.clear()
endDate.send_keys('2020-07-04')
#点击确定按钮
driver.find_element_by_css_selector('#c-tips-container > div:nth-child(1) > div > div > ul > li.c-tip-custom > a').click()









