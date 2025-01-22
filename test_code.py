#
#  test_code.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/22 10:54.
#


from PyStack import PyStack


# ======================= 以下为测试 PyStack 代码 ===============

# 1. 测试基本栈操作
def test():
    # 1. 创建一个空栈
    stack = PyStack()

    #  2. 输出判断栈是否为空
    print('stack 是否为空：{}'.format(stack.is_empty()))

    # 3. 入栈
    stack.push('steve')
    stack.push(100)
    stack.push('李四')

    # 4. peek() 以下
    print('stack.peek() {} '.format(stack.peek()))
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


# 判断给定的两个括号是否为同一类型括号
def is_match(left, right):
    lbs = '([{'
    rbs = ')]}'
    return lbs.index(left) == rbs.index(right)


# 2. 栈的应用，判断表达式中括号是否成对出现
def bracket_check(strcode):
    # 1. 创建一个空栈
    stack = PyStack()
    # 2. 声明一个标记变量，默认表示字符串中的括号是成对出现的
    balanced = True
    index = 0

    # 开始循环判断
    while index < len(strcode) and balanced:
        # 取出当前遍历的字符
        symbol = strcode[index]
        if symbol in '([{':
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                top = stack.pop()
                if not is_match(top, symbol):
                    balanced = False
        index = index + 1
    if balanced and stack.is_empty():
        return True
    else:
        return False


# 3. 进制转换


# 4. 表达式转换（中缀表达式、全括号表达式、前缀表达式、后缀表达式）
# 中缀表达式： a + b * c
# 前缀表达式： +a*bc
# 后缀表达式：abc*+
# 前缀和后缀表达式中，操作符的次序完全决定了运算的次序


if __name__ == '__main__':
    # 1. 调用 test() 测试方法
    # test()

    # 2. 调用测试括号是否成对出现
    print(bracket_check('{[]}'))
    print(bracket_check('()()(){}{}[]'))
    print(bracket_check('([)]'))
