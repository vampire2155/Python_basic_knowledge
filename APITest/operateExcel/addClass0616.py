import xlrd,json
from xlutils.copy import copy
from APITest.classManageAPI.add_class import addClassAPI

excelDir = r'G:\测试学习资料\接口测试\接口自动化测试_6-15\松勤-教管系统接口测试用例-v1.4.xls'
workBook = xlrd.open_workbook(excelDir,formatting_info=True) #保持原有格式不变
workSheet = workBook.sheet_by_name('2-课程模块')  #通过sheet页的名称获取sheet页
new_workBook = copy(workBook)  # 复制一个的新excel对象，即不操作原来的excel对象，不会修改原来的excel表。
new_workSheet = new_workBook.get_sheet(2)  #新的表
#封装成一个函数，方便循环执行所有增加课程的用例是调用该函数
def addClass(row):
    cellData = workSheet.cell_value(row,6) #获取excel用例中的请求参数信息
    tcNum = workSheet.cell_value(row,0) #获取excel用例中的用例标号
    #获取用例执行结果的retcode 值
    exeResult = json.loads(addClassAPI(cellData))["retcode"]  #json.loads() 是用来读取字符串的   json.load()是用来读取文件的。
    # print (exeResult)
    #获取用例中返回结果的code值
    expected_result = json.loads(workSheet.cell_value(row,8))["code"]
    # print (expected_result)
    if exeResult == expected_result:
        print (f'--------------用例编号为：{tcNum}的用例执行pass----------------')
        info = 'pass'  #用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    else:
        print(f'--------------用例编号为：{tcNum}的用例执行fail-----------------')
        info = 'fail'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    new_workSheet.write(row,9,info) #把执行结果写入到新的表中。

for row in range(1,26):
    addClass(row)

new_workBook.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\addclass_result.xls')



















