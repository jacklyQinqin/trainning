#可更改(mutable)与不可更改(immutable)对象
#在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

#不可变类型：变量赋值 a=5 后再赋值 a=10，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变a的值，相当于新生成了a。

#可变类型：变量赋值 la=[1,2,3,4] 后再赋值 la[2]=5 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

a = 3
b = [1,2,3,4]


#测试传递不可变对象
def TestMutable(s):
    s = 123123
    return
def TestImmutable(myList):
    myList.append(200)
    return
print(a)

TestImmutable(b)
print(b)

def f(a,b,*,c):
    return (a+b+c)

print(f(1,3,c=3))

