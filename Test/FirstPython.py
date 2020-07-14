#!/usr/bin/python
#encoding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from PIL import Image,ImageEnhance
import pytesseract
driver=webdriver.Chrome()
driver.get("http://www.songqinnet.com/login")
driver.maximize_window()
time.sleep(5)
'''
driver.implicitly_wait(5)属于隐式等待，5秒钟内只要找到了元素就开始执行，5秒钟后未找到，就超时；
time.sleep(5)表示必须等待5秒定位；
'''
driver.find_element_by_xpath('//*[@id="iframe_company_mini_div"]/h6/span[2]').click()
time.sleep(10)
driver.find_element_by_id('login_username').clear()  #清除输入框中内容
driver.find_element_by_id('login_username').send_keys("vampire2155")   #输入用户名
driver.find_element_by_id("login_password").clear()  #清除输入框中内容
driver.find_element_by_id("login_password").send_keys("ZHANGlei2155")  #输入密码
'''
怎么解决滑块的问题
1、可以使用微博登录跳过滑块验证
2、可以通过支付宝登录跳过滑块验证
'''
# while True:
#     try:
#         source=driver.find_element_by_id("nc_1_n1z")
#         ActionChains(driver).drag_and_drop_by_offset(source,258,0).perform()
#         time.sleep(2)
#         text=driver.find_element_by_xpath("//div[@id='nc_1__scale_text']/span")
#         if text.text.startswith(u'请在下方'):
#             print('成功滑动')
#         break
#         if text.text.startswith(u'请点击'):
#             print('成功滑动')
#         break
#         if text.text.startswith(u'请按住'):
#             continue
#     except Exception as e:
#         driver.find_element_by_id("BtnLogin").click()
#         print(e)
# time.sleep(20)
driver.save_screenshot('G:/Python_scripts/yzm1.png')  #截取登录界面的为图片并保存
yzm_element = driver.find_element_by_xpath('//*[@id="login-form"]/div[3]/div/a/img') #获取验证码元素的位置
yzm_location = yzm_element.location    # 获取验证码x,y轴坐标
print(yzm_location)
yzm_size = yzm_element.size   #获取验证码图片的大小   就是长和宽各是多少
print (yzm_size)
left = int(yzm_element.location['x'])  #验证码图片的下边线位置
upper = int(yzm_element.location['y'])   #验证码图片的左边线位置
right = int(yzm_element.location['x']) + int(yzm_element.size['width'])  #验证码图片的右边线位置
lower = int(int(yzm_element.location['y'])) + int(yzm_element.size['height'])  #验证码图片的上边线位置
print (lower, left, right, upper)
zuobiao = Image.open('/Test/yzm1.png')
yzm_frame = zuobiao.crop((left, upper, right, lower))  #使用crop()函数 对图片做裁切
yzm_frame = yzm_frame.convert('RGB')
yzm_frame.save('G:/Python_scripts/yzmframe.png')
text = pytesseract.image_to_string(Image.open('/Test/yzmframe.png'), lang='eng')
code = pytesseract.image_to_string(text).strip()
print (code.lower())
driver.find_element_by_xpath('//*[@id="login_verifi"]').send_keys(code.lower())
driver.find_element_by_xpath('//*[@id="login-form"]/div[5]/div/button').click()







