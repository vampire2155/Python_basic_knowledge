'''
题目要求：爬取51job网站中的招聘信息，并保存到excel中。
思路：
1、首先模拟浏览器发送请求，然后根据返回的信息（返回的请求信息，响应信息）获取到想要查找的数据
2、创建一个Excel，在excel中创建一个sheet页。
3、把爬取到的数据写入excel中
4、保存数据
'''

import xlwt
import re   #使用正则表达式获取数据时候需要用到 re 模块
import requests

workBook = xlwt.Workbook(encoding='utf-8')  #创建一个excel表格
workSheet = workBook.add_sheet('招聘信息')   #在创建的excel表格中，新增一个sheet页
web_url = 'https://search.51job.com/list/200200,000000,2720,01,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='

#headers中有很多内容，主要常用的就是user-agent 和 host，他们是以键对的形式展现出来，如果user-agent 以字典键对形式作为headers的内容，就可以反爬成功，就不需要其他键对；否则，需要加入headers下的更多键对形式。
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

#如果不加入headers 则会报错， 页面无法访问，这就是限制爬虫了。
respose = requests.get(web_url,headers=headers)
respose.encoding = 'gbk'  #如果不加这行代码，返回来的内容中有乱码,设置为 utf-8 编码也不行
title_info = re.findall('<div class="el title">(.*?)</div>',respose.text,re.S)   #获取返回数据中title信息
title = title_info[0]

#先把title获取到，然后写入excel中。
position_title = re.findall('<span class="t1">(.*?)</span>',title,re.S)[0]  #职位的标题
company_title = re.findall('<span class="t2">(.*?)</span>',title,re.S)[0]   #公司的标题
address_title = re.findall('<span class="t3">(.*?)</span>',title,re.S)[0]   #地址标题
salary_title = re.findall('<span class="t4">(.*?)</span>',title,re.S)[0]    #工资标题
rtime_title = re.findall('<span class="t5">(.*?)</span>',title,re.S)[0]     #发布日期的标题
title_list = [position_title,company_title,address_title,salary_title,rtime_title]   #把这些标题放在一个liest中进行写入操作。
for colum in range(len(title_list)):
    workSheet.write(0,colum,title_list[colum])  #write(行，列，内容)  行必须由 0 开始。写 1 的话，excel中会从第二行开始写入。

#然后获取数据并写入到excel中
data_info = re.findall('<div class="el">(.*?)</div>',respose.text,re.S)

#需要获取页面上数据的页数
def get_webPages():
    web_url = 'https://search.51job.com/list/200200,000000,2720,01,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url,headers=headers)
    resp.encoding = 'gbk'
    pages = re.findall('<span class="td">共(.*?)页，到第</span>',resp.text)[0]
    return int(pages)  #返回的pages是字符串，所以需要转换成 int 类型。

#这个循环是获取所有页中的数据并写入excel中。
line = 1
for pages in [1,get_webPages()+1]:
    web_url = f'https://search.51job.com/list/200200,000000,2720,01,9,99,%2520,2,{pages}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    resp = requests.get(web_url, headers=headers)
#下面的代码 职位名称、公司名称等没有使用循环来写。 --这个循环是获取一页的数据并写入excel中。
    for one in data_info:
        temp = re.findall('target="_blank" title="(.*?)" href',one,re.S)
        position = temp[0]  #职位名称
        workSheet.write(line,0,position)
        company = temp[1]   #公司名称
        workSheet.write(line, 1, company)
        address = re.findall('<span class="t3">(.*?)</span>',one,re.S)[0].strip()   #公司地址
        workSheet.write(line,2,address)
        salary = re.findall('<span class="t4">(.*?)</span>',one,re.S)[0].strip()    #薪资
        workSheet.write(line, 3, salary)
        rtime = re.findall('<span class="t5">(.*?)</span>',one,re.S)[0].strip()    #发布日期
        workSheet.write(line,4,rtime)
        line += 1
workBook.save(r'G:\Python_scripts\Test\UITest.xls')    #把上面的写入到缓存中的内容保存到excel中。

#下面把职位名称、公司名称等使用循环来写。  ---需要研究一下
# line = 1
# for one in data_info:
#     temp = re.findall('target="_blank" title="(.*?)" href',one,re.S)
#     position = temp[0]   #职位名称
#     company = temp[1]   #公司名称
#     address = re.findall('<span class="t3">(.*?)</span>',one,re.S)   #公司地址
#     salary = re.findall('<span class="t4">(.*?)</span>',one,re.S)    #薪资
#     rtime = re.findall('<span class="t5">(.*?)</span>',one,re.S)     #发布日期
#     data_list = [position, company, address, salary, rtime]
#     for data in range(0,len(data_list)):
#         workSheet.write(line, data, data_list[0])
#         workSheet.write(line, data, data_list[1])
#         workSheet.write(line, data, data_list[2])
#         workSheet.write(line, data, data_list[3])
#         workSheet.write(line, data, data_list[4])
#     line += 1















