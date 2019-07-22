#_*_coding:utf-8_*_
#!/usr/bin/env python
#在程序中，务必保证：先定义（类），后使用（产生对象）
#PS:
#  1. 在程序中特征用变量标识，技能用函数标识
#  2. 因而类中最常见的无非是：变量和函数的定义
import  os
import  random
class oldboystruct:
    school = 'oldboy'
    def learn(self):
        print("is learning")
    def eat(self):
        print("is eating ")
    def sleep(self):
        print("is sleeping ")



if __name__ == '__main__':
    a = oldboystruct()
    b = oldboystruct()
    a.eat()
    b.sleep()
    print(oldboystruct.__dict__)

    print(os.cpu_count())


#    while True:
#       print("random is %f",random.random())
    languages = ["C", "C++", "Perl", "Python"]
    for x in languages:
        print(x)