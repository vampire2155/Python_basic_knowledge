'''
1、用户控制台输入一个手机号，判断出运营商（移动、联通、电信）
2、输入位数不对，提示用户位数有误
3、输入非数字，提示非法字符
'''
'''
yidong = [150,158]
liantong = [132,156]
dianxin = [159,160]
telnum = input('Please input a phone number:')
if telnum.isdigit():   #判断输入的值是否为数字
    if len(telnum) != 11:
        print('电话号码位数有误!')
    else:
        if int(telnum[:3]) in yidong:  #telnum[:3]  是 str类型，如果不转换成 int ，则一直是 False。
            print('该号码是移动号码')
        elif int(telnum[:3]) in liantong:
            print('该号码是联通号码')
        elif int(telnum[:3]) in dianxin:
            print('该号码是电信号码')
        else:
            print ('输入的数字不是电话号码！')
else:
    print ('电话号码中存在非数字！')
'''

'''
以上代码存在的问题：
1、yidong、liantong、dianxin 这三个变量命令不规范，虽然比命名为 x,y,z强，但是建议最好使用英文单词命名。
China Telecom、China Mobile、China Unicom
2、yidong = [150,158]   列表中的元素类型使用不当， 最好使用 字符串类型。
原因：1）占用内存空间小 2）input()函数的结果是字符串类型，判断的时候不需要 str 类型和int 相互转换
3、telnum[:3] 没有使用变量，因为涉及多处，所以建议使用变量来替代，方便代码维护
'''

'''
#代码重新编写后见下面的代码
China_mobile = ['150','158']
China_Unicom = ['132','156']
China_Telecom = ['159','160']
telnum = input('Please input a phone number:')  #input() 函数的结果为 字符串类型。
if telnum.isdigit():   #检查字符串中是否都为 数字
# telnum.isalpha()   检查字符串中是否都是  字母
    if len(telnum) != 11:
        print('电话号码位数有误!')
    else:
        Top_Three = telnum[:3]
        if Top_Three in China_mobile:  #telnum[:3]  是 str类型，如果不转换成 int ，则一直是 False。
            print('该号码是移动号码')
        elif Top_Three in China_Unicom:
            print('该号码是联通号码')
        elif Top_Three in China_Telecom:
            print('该号码是电信号码')
        else:
            print ('输入的数字不是电话号码！')
else:
    print ('电话号码中存在非数字！')
'''
#循环代码结果如下：
China_mobile = ['150','158']
China_Unicom = ['132','156']
China_Telecom = ['159','160']
telnum = input('Please input a phone number:')  #input() 函数的结果为 字符串类型。
while True:
    if telnum.isdigit():   #检查字符串中是否都为 数字
        if len(telnum) != 11:
            print('电话号码位数有误，请重新输入！')
            telnum = input('Please input a phone number:')
        else:
            Top_Three = telnum[:3]
            if Top_Three in China_mobile:
                print('该号码是移动号码')
                break
            elif Top_Three in China_Unicom:
                print('该号码是联通号码')
                break
            elif Top_Three in China_Telecom:
                print('该号码是电信号码')
                break
            else:
                print ('输入的数字不是电话号码，请重新输入！')
                telnum = input('Please input a phone number:')
                Top_Three = telnum[:3]
    else:
        print ('电话号码中存在非数字，请重新输入！')
        telnum = input('Please input a phone number:')




