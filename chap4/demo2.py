# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 17:35
# 文件版本: V1.0.0
# 功能描述: Python 中一切皆对象，所有对象都有一个布尔值

# # 先要理解以下内容：
# # Python 中一切皆对象，所有对象都有一个布尔值
# # 获取对象的布尔值， 使用内置函数 bool()
# ## 以下对象的布尔值都为 False, 其它则都为 True
print (' -------以下对象的布尔值都为 False------- ')
# ## 1. False
print (bool(False))
# ## 2. 数值 0
print (bool(0))
print (bool(0.0))
# ## 3. None
print (bool(None))
# ## 4. 空字符串
print (bool(''))
print (bool(""))
# ## 5. 空列表
print (bool([]))
print (bool(list()))
# ## 6. 空元组
print (bool(()))
print (bool(tuple()))
# ## 7. 空字典
print (bool({}))
print (bool(dict()))
# ## 8. 空集合
print (bool(set()))

print (' -------其它对象的布尔值都为 True------- ')
print (bool(1))
print (bool("12w"))
