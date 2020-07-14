#获取excel中的用例并执行，最后把执行结果 回填到excel对应的列中。
import xlrd,json,requests
from xlutils.copy import copy
from APITest.classManageAPI.login import login
'''
思路：1、先打开excel文件并保持excel的样式不变化
     2、获取sheet页中有用的单元格的参数信息
     3、获取到信息后，调用已经写好的login接口，执行用例
     4、判断login接口用例执行的结果是否与excel中的预期结果一致，如果一致，则用例执行pass，如果不一致，则用例执行fail
     5、把执行结果写入到excel对应的单元格中。
'''
def login0616(username='auto',password='sdfsdfsdf'):
    HOST = 'http://127.0.0.1:9000'
    url = f'{HOST}/api/mgr/loginReq'
    headers = {'User-Agent': 'python-requests/2.23.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '311', 'Content-Type': 'application/x-www-form-urlencoded'}
    form_data = {
                'username':username,
                'password':password
                }
    # form_data = 'username=auto&password=sdfsdfsdf'  #data
    res = requests.post(url,data=form_data)
    res.encoding = 'unicode-escape'
    # cookie = res.cookies # 关联方法一：直接把返回的cookie值传递给需要的接口
    return res.json()

excelDir = r'G:\测试学习资料\接口测试\接口自动化测试_6-15\松勤-教管系统接口测试用例-v1.4.xls'
workBook = xlrd.open_workbook(excelDir,formatting_info=True)  #打开文件，返回一个实例。 formatting_info=True 表示保持源文件的样式（包括字体颜色，背景色等等样式）不变
#操作对应的sheet页
# workSheet = workBook.sheet_by_name('1_登录接口')  #通过sheet页的名称获取sheet页
workSheet = workBook.sheet_by_index(1)  #通过sheet页的下标获取sheet页

#然后把用例执行结果写入到excel中。但是为了保证原来的用例不发生变化，需要把用例复制一份，然后把用例执行结果写入到复制的excel中。
# 这样做的好处是不会改变用例中的数据。
new_workBook = copy(workBook) # 复制出来的新excel对象
new_workSheet = new_workBook.get_sheet(1) # 新的表
def login_OperExcel(row):
    #获取sheet页中的有用的单元格信息
    cellData = workSheet.cell_value(row,6)  #结果是一个字符串  ‘{"username": "auto","password": "sdfsdfsdf"}’
    tcNum = workSheet.cell_value(row,0)  #获取用例编号
    # print (cellData)  #因为结果是一个字符串，需要想要获取username和password，则需要将字符串 转换成json格式，用字典的方式获取值。

    # print (type(json.loads(cellData)))  #字典类型
    uName,psd = json.loads(cellData)['username'],json.loads(cellData)['password']

    #调用login接口 中的login函数
    res = login0616(username=uName,password=psd)['retcode']
    # print (type(res))  #int 型
    #获取用例中的返回结果单元格中的内容
    exp_result = workSheet.cell_value(row,8)  #结果是一个字符串，需要转换成字典以方便获取值
    result = json.loads(exp_result)['retcode']
    # print (type(result))  #int 型
    #现在判断 用例执行结果与 从excel中获取到的返回结果的值是否一致，如果一致则用例执行pass，如果不一致，则用例执行fail
    if res == result:
        print (f'--------------用例编号为：{tcNum}的用例执行pass----------------')
        info = 'pass'  #用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    else:
        print(f'--------------用例编号为：{tcNum}的用例执行fail-----------------')
        info = 'fail'  # 用例执行的结果赋值给一个变量，会在下面用例结果中写入时用到。
    new_workSheet.write(row,9,info)  #行下标 列下标 内容     把执行结果写入到新的excel中

#上面的函数是单条用例的执行过程，下面通过循环来执行sheet页中的所有用例
for one in range(1,5):  #sheet页中总共有4条用例
    login_OperExcel(one)

#然后保存excel
new_workBook.save(r'G:\测试学习资料\接口测试\接口自动化测试_6-15\result.xls')

if __name__ == '__main__':
    login0616(username='auto', password='sdfsdfsdf')









