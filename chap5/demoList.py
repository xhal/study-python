# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 22:16
# 文件版本: V1.0.0
# 功能描述: 列表对象的基本使用方法
'''
列表的特点：
    1、列表元素按顺序存储
    2、索引映射唯一一个数据
    3、列表可以存储重复数据
    4、任意数据类型混存
    5、根据需要动态分配和回收内存
'''

# 创建方式1： []
lst = [2, 3, 4, 5, 'hello', 'world', 1.123, 3]
print(id(lst))
print(type(lst))
print(lst)

print('--------------华丽的分隔线-----------------')
# 创建方式2： 内置函数 list()
lst1 = list([2, 3, 4, 5, 'hello', 'world', 1.123, 3])
print(id(lst1))
print(type(lst1))
print(lst1)

print(lst == lst1)
print(lst is lst1)

print('--------------华丽的分隔线-----------------')
# 对应索引位置值
print(lst[0], type(lst[0]))
print(lst[1], type(lst[1]))
print(lst[2], type(lst[2]))
print(lst[5], type(lst[5]))
print(lst[6], type(lst[6]))
# 负值索引 - 从后往前
print(lst[-1], type(lst[-1]))
print(lst[-2], type(lst[-2]))

print('--------------华丽的分隔线-----------------')
lst2 = lst[1:4:1]  # 开始索引，截止索引，步长
print(lst2)
# start:1 stop:5  step: 默认为1
print(lst[1:5])
# start:1 stop:5  step: 2
print(lst[1:5:2])
# start:默认0 stop:5  step: 2
print(lst[:5:2])
# start:默认0 stop:5  step: 默认1
print(lst[:5:])

print('--------------华丽的分隔线-----------------')
# start:默认0 stop:默认最后一个元素  step: -1
print(lst)
print(lst[::])
print(lst[::-1])  # 反转顺序输出

print('--------------华丽的分隔线-----------------')
# 获取索引位置
print(lst.index(3))  # 存在多个元素，仅返回第一个
print(lst.index('hello'))

print('--------------华丽的分隔线----------------- 添加元素 -----------------------')
lst.append(1)  # 在原 list 尾部，追加元素
print(lst)

print('--------------华丽的分隔线-----------------')
lst.insert(0, 11)  # 在原 list 指定索引位置，添加元素（索引位置，添加对象）
print(lst)

print('--------------华丽的分隔线-----------------')
lst.extend(lst1)  # 在原 list 尾部，追加至少一个元素（一般用于两list合并）
print(lst)

print('--------------华丽的分隔线-----------------')
lst3 = [True, False, 'test', 3, 4, 5, 8, 8]
# 切片添加，在任意位置上添加至少一个元素( 会将原 list 指定位置后的元素移除，再追加新的元素）
lst[3:] = lst3
print(lst)

print('--------------华丽的分隔线----------------- 移除元素 -----------------------')
# remove , 一次删除一个元素、重复元素删除第一个、元素不存在抛出异常
lst.remove(False)
print(lst)

obj = lst.pop(1)  # 按索引弹出元素，并在原 list 中移除
print(lst, ' pop obj:', obj)
obj = lst.pop()  # 不指定索引弹出元素，移除最后一个元素
print(lst, ' pop obj:', obj)

# 切片删除，一次至少删除一个元素, 将产生一个新的列表对象
newLst = lst[1:3]
print('原列表', lst)
print('新列表', newLst)
lst[1:3] = []
print('原列表', lst)

# clear 清空列表
lst.clear()
print('原列表', lst)

# del 删除对象
del lst
# print('原列表', lst) # 元素被删除，会抛出异常 NameError: name 'lst' is not defined

print('--------------华丽的分隔线----------------- 修改元素 -----------------------')
print(lst1)
lst1[2] = 'newVal'
print(lst1)
