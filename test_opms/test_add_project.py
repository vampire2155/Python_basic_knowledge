# -*- coding: UTF-8 -*- 
# @author  ：vampire
# @Time    : 2020/7/13 23:45
from test_opms.login import *
from time import sleep
import pytest,allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

@allure.feature('项目管理模块')
# @pytest.mark.flaky(reruns=3)   #装饰器，用例执行失败后会重新自动再执行3次
class Test_project_management():
    @allure.story('增加项目')
    @allure.title('增加项目用例')
    def test_addproj(self):
        with allure.step('步骤一、登录opms系统'):
            Login_class().login()
        with allure.step('步骤二、点击“项目管理”按钮'):
            driver.find_element_by_class_name('fa-book').click()
        with allure.step('步骤三、点击“新项目”按钮'):
            # driver.find_element_by_class_name('btn-success').click()
            driver.find_element_by_link_text('+新项目').click()
        sleep(1)
        with allure.step('步骤四、填写项目名称'):
            driver.find_element_by_css_selector('#project-form > div:nth-child(1)  input.form-control').send_keys('test_中国银行_2020-07-09')
        with allure.step('步骤五、填写项目别名'):
            driver.find_element_by_name('aliasname').send_keys('test_中国银行_2020-07-09')
        #填写开始日期
        start = driver.find_element_by_name('started')
        start.send_keys(Keys.CONTROL, 'a')
        start.send_keys(Keys.BACKSPACE)    # Keys.BACKSPACE == Keys.BACK_SPACE
        start.send_keys('2020-07-15')
        #填写结束日期
        end = driver.find_element_by_name('ended')
        end.send_keys(Keys.CONTROL, 'a')
        end.send_keys(Keys.BACK_SPACE)
        end.send_keys('2020-08-15')


       #项目描述是在 iframe框架里面，所以需要切入框架，然后再进行输入
        iframe = driver.find_element_by_class_name('ke-edit-iframe')
        driver.switch_to.frame(iframe)   #切入iframe框架
        #项目描述如下
        key_content = """该项目是一个中国银行的项目，开始于2020-07-09，结束与2020-08-09，周期为一个月。
        项目要求为：xxxxxxxx。
        项目验收时间为：2020-08-15日。
        """
        with allure.step('步骤六、填写项目描述'):
            driver.find_element_by_css_selector('body').send_keys(key_content)

        #现在需要切出框架，进行后面的点击提交按钮操作
        driver.switch_to.default_content()   #切出框架的操作
        sleep(1)
        with allure.step('步骤七、点击提交按钮'):
            driver.find_element_by_xpath('//*[@id="project-form"]/div[5]/div/button').click()
        #点击弹出框中的“去设置管理”按钮
        wait(driver, 3, 0.5, By.CSS_SELECTOR, '#projectModal a.btn.btn-primary').click()
        # driver.find_element_by_css_selector('#projectModal a.btn.btn-primary').click()
        nameEles = driver.find_elements_by_css_selector('#project-form-list td:nth-child(1) > a')
        namelist = []
        for ele in nameEles:
            namelist.append(ele.text)
        with allure.step('步骤八、判断项目是否增加成功'):
            assert 'test_中国银行_2020-07-09' in namelist
        driver.quit()


if __name__ == '__main__':
    pytest.main(['-s'])