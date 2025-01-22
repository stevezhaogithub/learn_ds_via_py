#
#  PyStack.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/22 10:37.
#
from operator import truediv


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


# ======================= 以下为测试 PyStack 代码 ===============

# 1. 创建一个空栈
stack = PyStack()

#  2. 输出判断栈是否为空
print('stack 是否为空：' + stack.is_empty())

# 3. 入栈
stack.push('steve')
stack.push(100)
stack.push('李四')

# 4. peek() 以下
print('stack.peek() ' + stack.peek())
stack.push(True)

# 5. 输出栈大小
print(stack.size())
print(stack.is_empty())

stack.push(8.4)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# 最后再输出栈大小
print(stack.size())
