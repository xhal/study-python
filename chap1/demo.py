# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/21 20:59
# 文件版本: V1.0.0
# 功能描述: print 使用

print(520)

# 不换行
print("this:", (520 + 556565.88565), "ssdfsdfsd", 'sdf222', 2 * 32 * 8 - 11 + 66)

print('sdf222222')

# 输出至文件
file1 = open('D:/python/test.sql', 'a+')
print('test hello world', file=file1)

file1.close()
