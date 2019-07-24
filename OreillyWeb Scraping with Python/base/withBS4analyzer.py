import html5lib
from bs4 import BeautifulSoup
from urllib.request import urlopen

"""
.findall的几种常用方法
    1.findall(标签字符串)
    2.findall(标签字符串列表)
    3.findall(标签,属性字典)
    4.findall(文本) 不以标签为查找的依据,而以实际的文本.将查找到的文本以列表的形式返回.
    5.findall(id) 指定属性,比如 id = "text"将返回所有的文本.
"""
try:
    html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
except:
    print("打开失败")

#bsObj = BeautifulSoup(html.read(),'html.parser') #默认解析器
#bsObj = BeautifulSoup(html,features="lxml")  #lxml解析器
bsObj = BeautifulSoup(html,features="html5lib") #html5lib解析器

# nameList = bsObj.findAll("span", {"class":"green"})
# print(nameList)
# print(type(nameList))
# for name in nameList:
#     print(name.get_text())
# #tag是一个字符串列表
# hlist = bsObj.findAll({"h1","h2","h3","h4","h5","h6"})
# print(hlist)
# for i in hlist:
#     print(i.get_text())
#属性是一个字典
a = bsObj.findAll("span",{'class':"green","class":'red'})
#print(a)
# for i in a:
#     print(i.get_text())
#
# nameList = bsObj.findAll(text="the prince")
# print( nameList)
# print(len(nameList))

# The  keyword  argument allows you to select tags that contain a particular attribute.
# For example:
#根据特定参数获取文本
allText = bsObj.findAll(id="text")
print(allText[0].get_text())


"""
#下面两行是相同的
bsObj.findAll(id="text")
bsObj.findAll("", {"id":"text"})
"""