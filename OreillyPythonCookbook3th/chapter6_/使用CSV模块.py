#CSV处理,感觉上应该是将打开的文件转成了树状结构体,或者是链表之类的特性.
#在打开之后f_csv对象就是一个链表的指针.

#
# import  csv
# with open("stocks.csv") as f:
#     f_csv = csv.reader(f)
#     header = next(f_csv)
#     #print(header)
#     for i in f_csv:
#         print(i)
#     print(f_csv)


#如果使用csv打开我司INI文件会如何?

import csv
with o