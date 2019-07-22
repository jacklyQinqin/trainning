#!usr/bin/env/python3
#Author ---qinxd
#company---istecc
#!/usr/bin/env python
# -*- coding: utf-8 -*-


#coding:utf-8

import urllib.request
import  urllib.response
# import urllib
# print(dir(urllib))
# for i in dir(urllib):
#     print(i)

#print("爬虫阶段1.初次使用")

import urllib.request
headers = {'User_Agent': ''}
response = urllib.request.Request('http://python.org/', headers=headers)
html = urllib.request.urlopen(response)
result = html.read().decode('utf-8')
print(result)

