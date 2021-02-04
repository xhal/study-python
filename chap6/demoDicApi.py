# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/2/4 22:32
# 文件版本: V1.0.0
# 功能描述: 字典常用方法

dic = {'a': 66, 'b': 'BB', 'c': 88.8, 'd': True}

# 获取所有的 key
keys = dic.keys()
print(keys, id(keys), type(keys))
# 转换成List
print(list(keys))

# 获取所有 value
vals = dic.values()
print(vals, id(vals), type(vals))
# 转换成List
print(list(vals))

# 获取所有键值对
items = dic.items()
print(items, id(items), type(items))
# 转换成List
print(list(items))

# 遍历
for item in dic:
    print(item, dic[item])
