# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 23:10
# 文件版本: V1.0.0
# 功能描述: 列表对象 - 排序

lst = [1, 3, 4, 5, 33, 2, 22, 11, 55, 66, 42]
print(id(lst), lst)
# 调用默认 sort(),默认为升序
lst.sort()

print(id(lst), lst)

# 调用默认 sort(reverse=True),降序
lst.sort(reverse=True)
print(id(lst), lst)

print('--------------华丽的分隔线-----------------')
# 内置函数 sorted()
lst = [1, 3, 4, 5, 33, 2, 22, 11, 55, 66, 42]
print(id(lst), lst)

nlst = sorted(lst)

print(id(lst), lst)  # 原列表不变
print(id(nlst), nlst)

nlst = sorted(lst, reverse=True)
print(id(lst), lst)  # 原列表不变
print(id(nlst), nlst)
