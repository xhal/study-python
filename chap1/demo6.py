# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/21 22:03
# 文件版本: V1.0.0
# 功能描述: <不同数据类型拼接/ 数据类型转换>

name = 'XH'
age = 22

print(type(name), type(age))

# print('我叫 ' + name + '， 今年' + age + '岁了') #TypeError: can only concatenate str (not "int") to str

print('我叫 ' + name + '， 今年' + str(age) + '岁了')

print("-----------------str() 将其它类型转成 str 类型")

a = 2
b = 3.33
c = True
print(type(a), type(b), type(c))

print(str(a), type(str(a)))
print(str(b), type(str(b)))
print(str(c), type(str(c)))

print("-----------------int() 将其它类型转成 int 类型")
s1 = '122'
f1 = 33.22
s2 = '88.22'
b1 = True
s3 = 'hi'

print(type(s1), type(f1), type(s2), type(b1), type(s3))
print(int(s1), type(int(s1)))
print(int(f1), type(int(f1)))  # 成功转换，丢失小数部分
# print(int(s2), type(int(s2)))  # ValueError: invalid literal for int() with base 10: '88.22'
print(int(b1), type(int(b1)))  # 成功转换
# print(int(s3), type(int(s3)))  # ValueError: invalid literal for int() with base 10: 'hi'

print("-----------------float() 将其它类型转成 float 类型")
s1 = '122.99'
s2 = '88.22'
s3 = 'hi'
i1 = 88
b1 = True
print(type(s1), type(s2), type(s3), type(i1), type(b1))
print(float(s1), type(float(s1)))
print(float(s2), type(float(s2)))
# print(float(s3), type(float(s3))) # ValueError: could not convert string to float: 'hi'
print(float(i1), type(float(i1)))
print(float(b1), type(float(b1)))
