from APITest.operateExcel.addClass0616 import addClass
from APITest.operateExcel.listClass0616 import listClass_OperExcel
from APITest.operateExcel.deleteClass0616 import deleteClass_OperExcel
import xlrd
from xlutils.copy import copy

excelDir = r'G:\测试学习资料\接口测试\接口自动化测试_6-15\松勤-教管系统接口测试用例-v1.4.xls'
workBook = xlrd.open_workbook(excelDir,formatting_info=True)
workSheet = workBook.sheet_by_name('2-课程模块')
new_workBook = copy(workBook)
new_workSheet = new_workBook.get_sheet(2)

for row in range(1,26):
    addClass(row)
    # print(new_workSheet.cell_value(row,9))
print ('******************************AddClassFinished***************************')
for row in range(26,38):
    listClass_OperExcel(row)
    # print(new_workSheet.cell_value(row,9))
print ('******************************ListClassFinished**************************')
for row in range(38,46):
    deleteClass_OperExcel(row)
    # print(new_workSheet.cell_value(row,9))
print ('******************************DeleteClassFinished*************************')
new_workBook.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\class_result.xls')  #保存结果

