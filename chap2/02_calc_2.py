# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/1/21 22:44
# 文件版本: V1.0.0
# 功能描述: <运算符 整除  取余  一正一负情况>

print(9 // 4)  # 2
print(-9 // -4)  # 2
print(-9 // 4)  # -3  一正一负，的整除公式，向下取整
print(9 // -4)  # -3  一正一负，的整除公式，向下取整

print(9 % -4)  # -3 公式:  余数 = 被除数 - 除数 * 商 [ 9 - （-4） * （-3） ====>  9 - 12  ===> -3 ]
print(-9 % 4)  # 3 [ -9 - （4） * （-3） ====>  -9 + 12  ===> 3 ]
