# coding:utf-8
# 版权信息: All rights Reserved, Designed By XHal.cc
# 代码作者: Hal
# 创建时间: 2021/7/28 19:00
# 文件版本: V1.0.0
# 功能描述: 自动移动鼠标，电脑不进入息屏

# 导入相关库
import pyautogui
import random
import time

# 使用while True循环，让程序一直执行！
while True:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    pyautogui.moveRel(x, y)

    print('x = ', x, '  , y = ', y)

    time.sleep(5)  # 让鼠标移动到某个位置，停留几秒钟，我怕它太累
