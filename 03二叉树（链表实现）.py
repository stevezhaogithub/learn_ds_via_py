#
#  03二叉树（链表实现）.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/25 17:13.
#

class BinaryTreeNode:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTreeNode(value)
        else:
            tNode = BinaryTreeNode(value)
            tNode.left_child = self.left_child
            self.left_child = tNode

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTreeNode(value)
        else:
            tNode = BinaryTreeNode(value)
            tNode.right_child = self.right_child
            self.right_child = tNode

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_value(self, value):
        self.key = value

    def get_root_value(self):
        return self.key


if __name__ == '__main__':
    # 创建一个空的二叉树
    btree = BinaryTreeNode('a')
    btree.insert_left('b')
    btree.insert_right('c')
    btree.get_right_child().set_root_value('hello')
    btree.get_left_child().insert_right('d')
    print(btree)
