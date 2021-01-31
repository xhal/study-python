# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 17:41
# 文件版本: V1.0.0
# 功能描述: 内置函数 range 的三种使用方法

# 作用： 生成一个整数的序列，返回值是一个迭代器对象
# 优点： 不管 range 对象表示的整数序列有多长，所有range 对象占用的内存空间都是相同的，因为仅仅需要存储 start/stop/step 三个参数，
#       只有当用到 range 对象时，才会去计算序列中的相关元素

# in  与  not in 判断整数序列中是否存在（不存在）指定的整数

# range(start, stop, step)  开始值、截止值、步长值
r1 = range(1, 13, 2)
print(r1)
print(list(r1))  # list 用于查看 range 对象中的整数序列， 即将 range 对象转换成 list 对象

print('--------------华丽的分隔线-----------------')

# range(start, stop)  开始值、截止值、默认步长值=1
r2 = range(1, 13)
print(r2)
print(list(r2))  # list 用于查看 range 对象中的整数序列， 即将 range 对象转换成 list 对象

print('--------------华丽的分隔线-----------------')
# range(stop)，只给一个参数  默认开始值= 0， 步长值 = 1
r = range(10)
print(r)
print(list(r))  # list 用于查看 range 对象中的整数序列， 即将 range 对象转换成 list 对象

print('--------------华丽的分隔线-----------------')
# in  / not in
print(10 in r)
print(9 in r)
print(9 not in r)
print(19 not in r)
print(1 not in r)
