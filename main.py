#
#  main.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/20 15:34.
#

import time


# 计算从 1 到 n 的累加和，通过迭代实现
def sumOfN(n):
    # 1. 获取执行开始时的时间
    start = time.time()
    total = 0
    for i in range(1, n + 1):
        total += i
    # 2. 获取执行结束后的时间
    end = time.time()

    # 3. 计算两者之间的差值
    seconds = end - start

    # 返回求和结果和执行时间的差值
    return total, seconds


# 计算从 1 到 n 的累加和，通过数学公式实现
def sumOfNViaFormula(n):
    start = time.time()
    total = ((1 + n) * n) / 2
    end = time.time()
    seconds = end - start
    return total, seconds


# 测试代码
print(sumOfNViaFormula(100000000))
print("=================================")
print(sumOfN(100000000))

# add a test
