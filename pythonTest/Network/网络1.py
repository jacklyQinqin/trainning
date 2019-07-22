"""
python 提供两个级别的访问的网络服务.
1.低级别的网络服务支持基本的socket.
提供了标准的BSD Socket api.可以访问底层操作系统的全部方法.
2.高级别的网络服务模块. socketServer.他提供了服务器中心类.
可以简化网络服务器的开发.
"""


#模式.1
#什么是socket.
#又称为套接字.应用程序同行通过 套接字 向网络发出请求或者应答网络请求.
#使主机间或者一台计算机上的进程间可以通讯.
#语法格式如下:
#socket.socket([family[, type[, proto]]])
#family: 套接字家族可以使AF_UNIX或者AF_INET
#type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
#protocol: 一般不填默认为0.

from urllib.request import  urlopen
html = urlopen("https://www.azure.cn/zh-cn/")
print(html.read())

