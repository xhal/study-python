# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/30 21:25
# 文件版本: V1.0.0
# 功能描述: <比较运算符  大于、等于、小于、大于等于、小于等于、不等于、is、is not>

a, b = 11, 22

print('a 大于 b ?', a > b)  # False
print('a 小于 b ?', a < b)  # True
print('a 等于 b ?', a == b)  # False
print('a 大于等于 b ?', a >= b)  # False
print('a 小于等于 b ?', a <= b)  # True
print('a 不等于 b ?', a != b)  # True

'''
    = 号为赋值运算符
    == 为比较运算符
    == 比较的为值？ 还是标识？  -- 比较的是值
    比较对象的标识是用 is
'''
c, d = 10, 10

print("c = ", c, 'id=', id(c), 'type=', type(c))
print("d = ", d, 'id=', id(d), 'type=', type(d))
print(c == d)  # True , value 相等
print(c is d)  # True , id标识 相等
print(c is not d)  # False , 判断 id标识 不相等

# list 结构
l1 = [1, 2, 3, 5, 6, 7]
l2 = [1, 2, 3, 5, 6, 7]

print("l1 = ", l1, 'id=', id(l1), 'type=', type(l1))
print("l2 = ", l2, 'id=', id(l2), 'type=', type(l2))
print(l1 == l2)  # True , 判断 value 相等
print(l1 is l2)  # False , 判断 id标识 相等
print(l1 is not l2)  # True , 判断 id标识 不相等
