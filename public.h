#ifndef __PUBLIC_H__
#define __PUBLIC_H__

/********
常用的函数描述.和定义.
不牵涉硬件参数的,只牵涉算法部分的函数.在此实现.
牵涉硬件功能的.在这里统一定义.
目的是为了以后项目中可以在调试阶段或者发布阶段使用一些常用的
函数.
举例说明:
	1.不牵涉硬件的,在这里实现.
	2.牵涉硬件的.只定义.在具体的项目中实现.
	PrintLog(str,len)
		
********/

//类型1
void HexToString();
void StringToHex();



//类型2:
void PrintLog(unsigned char *str,unsigned int len);




#endif
