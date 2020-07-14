import xlrd,json
from APITest.classManageAPI.list_class import listClassAPI
from xlutils.copy import copy
excelDir = r'G:\测试学习资料\接口测试\接口自动化测试_6-15\松勤-教管系统接口测试用例-v1.4.xls'
workBook = xlrd.open_workbook(excelDir,formatting_info=True) #保持原有的样式不变
workSheet = workBook.sheet_by_name('2-课程模块')  #通过sheet页的名称获取sheet页
new_workBook = copy(workBook)
new_workSheet = new_workBook.get_sheet(2)  #通过下标获取sheet页

#封装成一个函数，方便循环执行所有列出课程的用例是调用该函数
def listClass_OperExcel(row):
    cellData = json.loads(workSheet.cell_value(row,6))
    tcNum = workSheet.cell_value(row,0) #获取excel中的用例编号
    EXEresult = listClassAPI(cellData)['retcode']  #用例的执行结果
    expected_result = json.loads(workSheet.cell_value(row,8))['code']  #获取用例中的返回结果
    if EXEresult == expected_result:
        print(f'--------------用例编号为：{tcNum}的用例执行pass----------------')
        info = 'pass'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    else:
        print(f'--------------用例编号为：{tcNum}的用例执行fail-----------------')
        info = 'fail'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    new_workSheet.write(row,9,info)  #(行,列,内容)    #把执行结果写入到新的表中

for row in range(26,38):
    listClass_OperExcel(row)
new_workBook.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\listclass_result.xls')  #保存执行结果。
# 经验证，上面的save()函数是 每次会新生成一个excel，然后把之前的覆盖掉。









