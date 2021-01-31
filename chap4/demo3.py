# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/31 17:35
# 文件版本: V1.0.0
# 功能描述: 程序的组织结构  - 计算机的流程控制： 选择(分支)结构

# 选择(分支)结构： if语句

'''  单分支结构
  if 条件表达式:
     符合条件的执行代码
'''
money = 10000  # 余额

# 输入取款金额
qu = int(input('请输入取款金额：'))

print ('------- 单分支结构 -------- ')
if money >= qu:
    money -= qu
    print ('取款成功，余额为：', money)
    # print 带第二个参数 money ,中文会打印输出以下内容，why?  使用的python版本为 2.7  切换为 3.9 以后不会
    # '\xe5\x8f\x96\xe6\xac\xbe\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8c\xe4\xbd\x99\xe9\xa2\x9d\xe4\xb8\xba\xef\xbc\x9a'

print ('------- 双分支结构 -------- ')
'''  双分支结构
  if 条件表达式:
     符合条件的执行体
  else
     其它条件执行体
'''
if money >= 5000:
    print ('余额大于等于 5000')
else:
    print ('余额不足 5000')

print ('------- 多分支结构 -------- ')
'''  多分支结构
  if 条件表达式:
     符合条件的执行体
  elif 条件表达式2:
     执行体2
  elif 条件表达式3:
     执行体3
  else
     其它条件执行体
'''
if money >= 9000:
    print ('余额大于等于 9000')
elif money >= 8000:
    print ('余额大于等于 8000')
elif money >= 7000:
    print ('余额大于等于 7000')
else:
    print ('余额不足 7000')

print ('------- 嵌套if -------- ')
''' 嵌套if
  if 条件表达式:
    if 条件表达式:
      执行体0
    else 
      执行体1
  else 
    其它执行体
'''
if money > 5000:
    if money >= 8000:
        print ('大于等于 8000')
    else:
        print ('小于 8000，大于5000')

else:
    print ('小于等于5000')

print ('------- 条件表达式 即if else 简写 -------- ')
num_a = 100
num_b = 88
# 正常逻辑，写if
if num_a >= num_b:
    print (num_a, 'if 大于等于', num_b)
else:
    print (num_a, 'if 小于', num_b)

# 条件表达式写法 , if 条件为 True 时，执行左边内容， False 时，执行else 右边内容
print ((num_a, 'S 大于等于', num_b) if num_a >= num_b else (num_a, 'S 小于', num_b))
