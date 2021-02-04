# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/2/4 22:26
# 文件版本: V1.0.0
# 功能描述: 字典的 key 的判断、新增、修改、删除
'''
    字典的特点：
        1、所有元素都是一个key/value对，key 不允许重复、value可以重复
        2、字典中的元素是无序的
        3、字典中的key必须是不可变对象
        4、字典也可以根据需要动态伸缩
        5、字典会浪费较大的内存，是一种使用空间换时间的数据结构
'''

dic = {'a': 66, 'b': 'BB', 'c': 88.8, 'd': True}

# 判断key 是否存在
print('a' in dic)
print('f' in dic)
print('a' not in dic)
print('g' not in dic)

# 增加、修改、删除 - 与 js 基本一致
# 新增
dic['aa'] = 33
print(dic)

# 修改
dic['a'] = 68
print(dic)

# 删除
del dic['d']
print(dic)

# 清空方法
dic.clear()
print(dic)
