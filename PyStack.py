#
#  PyStack.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/22 10:37.
#

# 用 Python 模拟栈数据结构

class PyStack:

    # 1. 初始化一个空栈
    def __init__(self):
        self.items = []

    # 2. 判断栈是否为空
    def is_empty(self):
        return self.items == []

    # 3. 入栈操作
    def push(self, item):
        self.items.append(item)

    # 4. 出栈操作
    def pop(self):
        return self.items.pop()

    # 5. 查看栈顶元素, 但不出栈
    def peek(self):
        return self.items[len(self.items) - 1]

    # 6. 返回栈中元素个数
    def size(self):
        return len(self.items)
