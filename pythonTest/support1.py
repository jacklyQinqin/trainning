#!/usr/bin/python3
# Filename: support.py
#说明:放在pycharm的根目录底下,默认是可以被路径搜索的.
def print_func(par):
    print("Hello : ", par)
    return


if __name__ == '__main__':
   print('模块当主模块的时候,程序自身在运行')
else:
   print("只有在第一次导入模块的时候,可执行的语句被执行")