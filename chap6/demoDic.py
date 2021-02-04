# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/2/4 22:08
# 文件版本: V1.0.0
# 功能描述: 字典对象 - 基础使用

# 创建方式1：{}  花括号，与javascript Object 一样
# 空字典
dic = {}
print(dic)
# 键: 值
dic = {'a': 'aa', 'b': 3}
print(dic, id(dic), type(dic))

# 创建方式2： 内置函数
dic1 = dict({'a': 'aa', 'b': 3})
print(dic1, id(dic1), type(dic1))

print(dic == dic1)
print(dic is dic1)

# 创建方式2： 内置函数(左侧键，不加引号; 右侧值则根据对应类型)
dic2 = dict(a='aa', b=3)
print(dic2, id(dic2), type(dic2))

print(dic == dic2)
print(dic is dic2)
