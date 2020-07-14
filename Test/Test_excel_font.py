import xlwt
style = xlwt.XFStyle()#格式信息
font = xlwt.Font()#字体基本设置
font.name = u'微软雅黑'
font.color = 'black'
font.height= 220 #字体大小，220就是11号字体，大概就是11*20得来的吧
style.font = font
alignment = xlwt.Alignment() # 设置字体在单元格的位置
alignment.horz = xlwt.Alignment.HORZ_CENTER #水平方向
alignment.vert = xlwt.Alignment.VERT_CENTER #竖直方向
style.alignment = alignment
# border = xlwt.Borders()  #给单元格加框线
# border.left = xlwt.Borders.THIN  #左
# border.top=xlwt.Borders.THIN     #上
# border.right=xlwt.Borders.THIN   #右
# border.bottom=xlwt.Borders.THIN  #下
# border.left_colour = 0x40  #设置框线颜色，0x40是黑色，颜色真的巨多，都晕了
# border.right_colour = 0x40
# border.top_colour = 0x40
# border.bottom_colour = 0x40
# style.borders = border
#写入sheet
row=0
col=0
value=100
wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
ws.write(row,col,value,style)#这样就可以写入自己想要的格式了
wb.save(r'G:\Python_scripts\Test\Test_font.xls')
