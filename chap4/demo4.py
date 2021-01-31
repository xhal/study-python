# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 17:41
# 文件版本: V1.0.0
# 功能描述: pass 语句

# pass 语句，什么都不做，只是一个点位符，用在语法上需要语句的地方

# 什么时候用： 先搭建语法结构，但还没想好内部代码怎么写的时候

# 用在什么语句中：
# 1、if 语句的条件执行体
answer=input('您是会员吗？y/n')

# 判断是否为会员
if answer == 'y':
    pass
else:
    pass

# 2、for-in 语句的循环体
for i in range(5):
    pass

# 3、定义函数时的函数体
