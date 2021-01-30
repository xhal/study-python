# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/21 20:59
# 文件版本: V1.0.0
# 功能描述: 转义字符

print('hello\nworld') # \ + 转义功能的首字母  n  --> newline 的首字母
print('----------------------------')
print('hello\rwor')  # \r  回车，回车至首字母，将hello 清空了
print('----------------------------')
print('hello\tworld')  # \t   tab  制表符
print('----------------------------')
print('hello\bworld')   # \b 是退一个格，将 o 干没了
print('----------------------------')

print('http://www.xhal.cc\\?ss')
print('老师说： \'大家好\'')
print('老师说： "大家好"')
print("老师说： \"大家好\"")
print('老师说： \"大家好\"')

# 原字符，不希望字符串中的转义字符起作用，就使用原字符，在字符串前加上 r 或 R
print(r'hello\nworld')
print(R'hello\rwor')