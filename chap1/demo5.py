# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/21 21:43
# 文件版本: V1.0.0
# 功能描述: 基础数据类型 demo   int / float / bool / str

# int  - 整数可以表示， 二进制、八进制、十进制(默认)、十六进制
print('二进制', 0b11111)  # 0 零 b 英文字母B
print('八进制', 0o117)  # 0 零 o 英文字母O
print('十进制', 118)  # (默认)
print('十六进制', 0x1188) # 0 零 x 英文字母X

print('--------------华丽的分隔线-----------------')
# float
a = 3.141592654
print('a',a)

b=2.2
print('b:', b)
print('a + b:', a+b)
print('b + 1.1:', b+1.1) # 浮点数，不精确， 如果要精确，引入 decimal 处理

print('--------------华丽的分隔线-----------------')
# bool
bo = True
print('bo:', bo)

bo2= False
print('bo2:',bo2)

#bool 可以当作整数计算 True = 1, False = 0
print('bo + 1=', bo + 1)
print('bo2 + 1=', bo2 + 1)
print('bo + bo2=', bo2 + bo)

print('--------------华丽的分隔线-----------------')
# str
# 单引号  - 只能在一行
s1 = '人生苦短， hello world'
print(s1, type(s1))

# 双引号  - 只能在一行
s2 = "人生苦短， hello world"
print(s2, type(s2))

# 三引号（单引号） - 可多行输入字符串
s3 = '''单:这是第一行
，第二行
，第三行'''
print(s3, type(s3))

# 三引号（双引号） - 可多行输入字符串
s3 = """双:这是第一行
，第二行
，第三行"""
print(s3, type(s3))