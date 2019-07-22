#!/usr/bin/python3
# Filename: support.py

#较为全面的介绍类, 子类,和类的参数,方法.
#1.如何定义类.
#2.定义一些基本属性.
#3.定义一些私有属性.使用 __属性来定义.私有属性不能直接用实例或者类来访问.但是可以通过方法来访问. 私有方法也是同理
#4.定义构造方法.第一个参数是self
#5.定义基本的方法.参数默认第一个self
#6.实例化类
#7.继承在类创建的时候,在类名()内加入父类名即可.
#8重写.子类重写父类的方法.在子类的实例化中,调用的是新的方法.这种操作叫做override
#9实例化子类
#10多继承.如果方法相同. 则从左到右搜索.
class  people:  #1.定义一个类.
    #2.定义基本属性
    name = ''
    age = 0
    #3.定义一些私有属性
    __weight = 0
    #4.定义构造方法
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    #5.定义普通的方法
    def speak(self):
        print(" {0} says: my age is {1}".format(self.name,self.age))


#7.继承.比如中国人继承人.
class  chinese(people):
    country = "Chinese"
    #8重写.
    def speak(self):
        print(" {0} says: my age is {1},and i 'm from {2}".format(self.name, self.age,self.country))
#6.实例化类
p = people('jack','12',100)
p.speak()
#9实例化子类
p1 = chinese("qinxd",'13',300)
p1.speak()
