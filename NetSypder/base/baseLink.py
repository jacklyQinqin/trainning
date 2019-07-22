from urllib.request import urlopen
from bs4 import BeautifulSoup
"""
b'<html>\n<head>\n<title>A Useful Page</title>\n</head>\n<body>\n<h1>An Interesting Title</h1>\n
<div>\nLorem ipsum dolor sit amet, consectetur adipisicing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
 aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse 
 cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, 
 sunt in culpa qui officia deserunt mollit anim id est laborum.\n</div>\n</body>\n</html>\n'
"""

"""
** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** **
重要说明:
直接使用urlopen可能导致异常.
原因是: 1.
网页不存在
2.
主机不存在等.
方法: 使用try.

"""


#html = urlopen("http://pythonscraping.com/pages/page1.html")
#html = urlopen("file:///C:/Users/jk/Desktop/A%20Useful%20Page.html")
# html = urlopen("https://mbd.baidu.com/newspage/data/landingsuper?context=%7B%22nid%22%3A%22news_9521665027372867584%22%7D&n_type=0&p_from=1")
# print(html.read())

from urllib.request import urlopen
from bs4 import BeautifulSoup
#正确实例
#html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#错误实例1 不存在网页
#html = urlopen("http://www.123qwe.com/pages/page1.html")
# try:
#     html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# except:
#     print("捕获到错误")
# else:
#     print("未捕获错误则执行")
#     #print(html.read())
#     bsObj = BeautifulSoup(html.read(),'html.parser')
#     print(bsObj.h1)
#     print(bsObj.html.h1)
#     print(bsObj.body.h1)
#     print(bsObj.html.body.h1)
#
#     print(bsObj.nonExistent)
#
# finally:
#     print("结束,肯定会执行")
#


# #print(html.read())
# bsObj = BeautifulSoup(html.read(),'html.parser')
#
#
# print(bsObj.h1)
# print(bsObj.html.h1)
# print(bsObj.body.h1)
# print(bsObj.html.body.h1)


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)


title = getTitle("https://www.runoob.com/python/python-for-loop.html")
if title == None:
    print("Title could not be found")
else:
    print(title)


