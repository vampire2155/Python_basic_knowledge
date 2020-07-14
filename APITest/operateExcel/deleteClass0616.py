import xlrd,json
from APITest.classManageAPI.delete_class import deleteClassAPI
from xlutils.copy import copy
from APITest.classManageAPI.delete_class import deleteClassAPI

excelDir = r'G:\测试学习资料\接口测试\接口自动化测试_6-15\松勤-教管系统接口测试用例-v1.4.xls'
workBook = xlrd.open_workbook(excelDir,formatting_info=True)
workSheet = workBook.sheet_by_name('2-课程模块')
new_workBook = copy(workBook)
new_workSheet = new_workBook.get_sheet(2)

#封装成一个函数，方便循环执行所有删除课程的用例是调用该函数
def deleteClass_OperExcel(row):
    cellData = json.loads(workSheet.cell_value(row,6))  #获取单元格中的数据
    tcNum = workSheet.cell_value(row,0)  #获取excel中的用例编号
    EXEresult = deleteClassAPI(cellData)['retcode']  #通过调用函数deleteClassAPI()获取执行结果
    # print (EXEresult)
    expected_result = json.loads(workSheet.cell_value(row,8))['code']  #从excel表用例中获取返回结果
    # print (expected_result)
    if EXEresult == expected_result:
        print(f'--------------用例编号为：{tcNum}的用例执行pass----------------')
        info = 'pass'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    else:
        print(f'--------------用例编号为：{tcNum}的用例执行fail-----------------')
        info = 'fail'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    new_workSheet.write(row,9,info)

for row in range(38,46):
    deleteClass_OperExcel(row)

new_workBook.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\deleteclass_result.xls')  #保存结果




