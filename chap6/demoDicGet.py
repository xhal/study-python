# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/2/4 22:21
# 文件版本: V1.0.0
# 功能描述: 字典的取值

dic = {'a': 66, 'b': 'BB', 'c': 88.8, 'd': True}

# 取值方式1： dic[key]
print(dic['c'])

# print(dic['f']) # 查找的键不存在，抛出异常：  KeyError: 'f'

# 取值方式2： dic.get(key)
print(dic.get('a'))

print(dic.get('f')) # 查找的键不存在，返回 None

# 默认值
print(dic.get('f', 99)) # 查找的键不存在，返回 第二个参数（默认值）
