# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 17:41
# 文件版本: V1.0.0
# 功能描述: 程序的组织结构  - 计算机的流程控制：循环结构

# while 循环
a = 10
while a > 0:
    print('current a : ', a)
    a -= 1

print('--------------华丽的分隔线-----------------')
'''计算 1 ~ 100 间的偶数和'''
sum = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1

print('1 ~ 100 间的偶数和=', sum)

print('--------------华丽的分隔线-----------------')
# for 循环:   for 自定义变更   in  可迭代对象
r = range(11)
for i in r:
    print('i = ', i)

print('--------------华丽的分隔线-----------------')
for c in 'Python helloWorld':
    print('c = ', c)

# 如果在 循环体中不需要用到自定义变量，可将自定义变量写为 "_"
for _ in range(3):
    print('test_iii+')

print('--------------华丽的分隔线-----------------')
'''
    输入100 ~ 999 内的水仙花数
    水仙花数： 当前数 = 每个数字的立方和 
    如： 153 = 1*1*1 + 5*5*5 + 3*3*3
'''
for i in range(100, 1000):
    bai = i // 100  # 百位
    shi = i // 10 % 10  # 十位
    ge = i % 10  # 个位
    # print(bai, shi, ge)
    if bai ** 3 + shi ** 3 + ge ** 3 == i:
        print('水仙花数：', i)


print('--------------华丽的分隔线-----------------')
# break    跳出循环（退出循环结构）
for i in range(10):
    if i > 5:
        break
    print('i：', i)

print('--------------华丽的分隔线-----------------')
# continue 结束当前循环（本次循环后续代码不执行），直接进入下次循环
for i in range(10):
    if 5 <= i <= 7:
        continue
    print('i：', i)

print('--------------华丽的分隔线-----------------')
# 嵌套循环
for i in range(5):
    for j in range(6):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

print('--------------华丽的分隔线-----------------')
# 嵌套循环
for i in range(1,10):
    for j in range(1, i+1):
        print('*', end='\t')  # 不换行输出
    print()  # 换行

print('--------------华丽的分隔线-----------------')
# 嵌套循环  9/9 乘法表
for i in range(1,10):
    for j in range(1, i+1):
        print(i,'*',j,'=', i*j, end='\t')  # 不换行输出
    print()  # 换行
