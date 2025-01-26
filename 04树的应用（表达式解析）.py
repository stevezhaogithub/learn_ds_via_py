#
#  04树的应用（表达式解析）.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/25 17:33.
#


'''
# 1. 通过 split() 将字符串分割成 list
expr = '3 + ( 4 * 5 )'
nodes = expr.split(' ')
print(nodes)

'''
from BinaryTreeNode import BinaryTreeNode
from PyStack import PyStack
import operator

'''

# 2. 直接字符串转 list
expr = '3+(4*5)'
nodes = list(expr)
print(nodes)

'''

# 根据表达式字符串，构建一个表达式二叉树
'''
    1. 参数 expr 是没有空格的表达式
'''


def build_expression_tree(expr):
    # 1. 将表达式拆分成 tokens list
    tokens = list(expr)

    # 2. 创建一个栈数据结构
    stack = PyStack()

    # 3. 创建一个二叉树对象（即一个空的二叉树根节点，根节点数据为 ''）
    btree = BinaryTreeNode('')

    # 4. 将根节点压入栈中
    stack.push(btree)

    # 5. 创建一个用来指示当前节点的变量
    current_node = btree

    # 6. 循环 tokens 中的每个 token， 并进行判断
    for token in tokens:
        if token == '(':
            # 创建左子节点，并将当前节点设置为左子节点
            current_node.insert_left('')
            stack.push(current_node)
            current_node = current_node.get_left_child()
        elif token not in ['+', '-', '*', '/', ')']:
            current_node.set_root_value(int(token))
            parent_node = stack.pop()
            current_node = parent_node
        elif token in ['+', '-', '*', '/']:
            current_node.set_root_value(token)
            current_node.insert_right('')
            stack.push(current_node)
            current_node = current_node.get_right_child()
        elif token == ')':
            current_node = stack.pop()
        else:
            raise ValueError
    return btree


# 递归方式计算表达式的值
def evaluate(etree: BinaryTreeNode):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left_tree = etree.get_left_child()
    right_tree = etree.get_right_child()
    if left_tree and right_tree:
        fn = opers[etree.get_root_value()]
        return fn(evaluate(left_tree), evaluate(right_tree))
    else:
        return etree.get_root_value()
