#模块 放在  包 下面
#文件夹 一般存放  一些配置文件等。
def sum(a,b):
    print (a+b)

#内置变量  __name__
#运行本模块，该模块的__name__ 就是  __main__   相当于程序的入口
# print (__name__)    #打印结果为：  __main__

#如果模块被其他模块调用， __name__  就是该模块的模块名

if __name__ == '__main__':   #这条语句的作用：1、程序的入口   2、调试时使用   #这条语句  在本模块被其他模块调用时也不需要删除。
    sum(2,3)