'''
类：一类事物的统称   比如，老虎，是东北虎、华南虎、等等其他一些种类的 老虎的统称。
类的定义：关键字 class + 类名()    类名的首字母一般是大写的。
    1、特征   ---俗称(比如 人 这个类  的外貌特征)
       术语   ---属性
       本质   ---变量
    2、行为   ----俗称 (比如 人 这个类  的行为： 会吃饭、睡觉、看书等等一些行为特征)
       术语   ----方法
       本质   ----函数
'''
class Person():  #这个是创建一个类    --类的首字母要大写
    nickName = '人类'   #这个是类属性， 这个类里面的所有的实例都共有的一个属性，比如： 张三的 类属性是 人类，李四的类属性也是人类。

    #下面这个函数是 实例属性   每一个实例的实例属性都不一样， 比如张三和李四的 名字、年龄、体重等等属性都不一样。
    def __init__(self,inName,inAge,inWeight):  #初始化方法，创建实例时自动会调用该方法。
        self.name = inName   #self--谁调用就是谁，比如 p1 这个实例调用的时候，就表示 p1， p2这个实例调用的时候就表示 p2
        self.age = inAge
        self.weight = inWeight

    #下面这是函数  是 实例方法.
    def eat(self):  #self--谁调用就是谁，比如 p1 这个实例调用的时候，就表示 p1， p2这个实例调用的时候就表示 p2
        self.weight += 1
        print (f'我刚吃完饭，我现在的体重是{self.weight}斤。')

#实例的创建  --创建实例   --类名()
p1 = Person('Jack',20,140)  #这个就是创建实例，这时候就会自动调用类中的  初始化方法 __init__()
# print (f'{p1.name} 是 {p1.nickName}')   #打印结果为：  Jack 是 人类
p1.eat()


'''
class Person:
    nickName = '人类'#类属性--这个类所有的实例都是一样的--共有的
    #对于实例，有些属性每一个实例是不一样的？--实例属性：属于实例
    def __init__(self,inName,inAge,inWeight):#初始化方法--创建实例会自动化调用
        # print('我执行了！',self)
        self.name = inName
        self.age = inAge
        self.weight = inWeight
    #实例方法---实例调用
    def eat(self):
        self.weight += 10
        print('我在吃饭！--我立马重了10斤',self.weight)

    #类方法--类调用的  实例调用也可以
    @classmethod
    def tell(cls):
        cls.nickName = 'xxxxx'
        print('我是类方法')

    #静态方法
    @staticmethod
    def run():
        print('----静态方法---')


#2- 创建实例  类名()
p1 = Person('tom',20,160)
p2 = Person('jack',30,150)
print (p1.run.nickName)
'''


