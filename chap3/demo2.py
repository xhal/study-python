# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/30 21:40
# 文件版本: V1.0.0
# 功能描述: <布尔运算符  and / or / not / in / not in>

a, b = 22, 33
print('------ and  ')
print(a == 22 and b == 33)  # True and True   = True
print(a == 22 and b != 33)  # True and False  = False
print(a != 22 and b == 33)  # False and True  = False
print(a != 22 and b != 33)  # False and False = False


print('------ or  ')
print(a == 22 or b == 33)  # True or True   = True
print(a == 22 or b != 33)  # True or False  = True
print(a != 22 or b == 33)  # False or True  = True
print(a != 22 or b != 33)  # False or False = False


print('------ not 仅可对 Bool 取反（相当于 java 里的 ! ） ')
b1 = True
b2 = False
print(not b1)  # False
print(not b2)  # True

print('------ in / not in')
s1 = 'hellwordtest'
print('w' in s1)
print('word' in s1)
print('word' not in s1)
print('x' not in s1)

