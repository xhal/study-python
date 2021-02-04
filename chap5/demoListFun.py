# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/2/4 21:57
# 文件版本: V1.0.0
# 功能描述: List 创建方法： 表达式方法(有规律的数据，可用表达式生成)
# 1 ~ 9
lst = [i for i in range(1, 10)]
print(lst)

# 2 4 6 8 10
lst = [i*2 for i in range(1, 6)]
print(lst)

# 1=1*1, 4=2*2, 9=3*3, 16=4*4, 25=5*5
lst = [i*i for i in range(1, 6)]
print(lst)
