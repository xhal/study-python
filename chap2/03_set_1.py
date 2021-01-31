# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/27 20:01
# 文件版本: V1.0.0
# 功能描述: <赋值运算符 - 执行顺序，从 右 到 左>

# 最简单赋值
a = 2
print("a = ", a)
print('--------------华丽的分隔线-----------------')

# 带运算赋值
a = 2 + 3
print("a = ", a)
print('--------------华丽的分隔线-----------------')

# 链式赋值 - 相同ID,内存地址相同
a = b = c = 22
print("a = ", a, 'id=', id(a))
print("b = ", b, 'id=', id(b))
print("c = ", c, 'id=', id(c))

# 单独改变 C 的 值， a、b 不变， a、b的id也不变
c = c + 3
print("a = ", a, 'id=', id(a))
print("b = ", b, 'id=', id(b))
print("c = ", c, 'id=', id(c))
print('--------------华丽的分隔线-----------------')

# += 、 -=  、 *=  、 /=  、  //= 、  %=
a += 5  # 相当于  a = a + 5
print("a = ", a, 'id=', id(a), 'type=', type(a))
a -= 8  # 相当于  a = a - 8
print("a = ", a, 'id=', id(a), 'type=', type(a))
a *= 8  # 相当于  a = a * 8
print("a = ", a, 'id=', id(a), 'type=', type(a))
a /= 8  # 相当于  a = a / 8
print("a = ", a, 'id=', id(a), 'type=', type(a))
a //= 8  # 相当于  a = a // 8
print("a = ", a, 'id=', id(a), 'type=', type(a))
a %= 8  # 相当于  a = a % 8
print("a = ", a, 'id=', id(a), 'type=', type(a))

print('--------------华丽的分隔线-----------------')
# 解包赋值
a, b, c = 10, 22, 33

print("a = ", a, 'id=', id(a), 'type=', type(a))
print("b = ", b, 'id=', id(b), 'type=', type(b))
print("c = ", c, 'id=', id(c), 'type=', type(c))

# 左右数量不匹配，异常
# a,b = 1,2,3   ValueError: too many values to unpack (expected 2)


print('--------------华丽的分隔线-----------------')
# 两个变量，交换赋值
a, b = b, a

print("a = ", a, 'id=', id(a), 'type=', type(a))
print("b = ", b, 'id=', id(b), 'type=', type(b))
