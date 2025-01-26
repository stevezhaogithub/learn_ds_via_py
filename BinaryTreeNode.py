#
#  BinaryTreeNode.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/26 09:49.
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

    # 先序遍历
    def pre_order(self):
        print(self.key)
        if self.left_child is not None:
            self.left_child.pre_order()
        if self.right_child is not None:
            self.right_child.pre_order()

    # 后序遍历
    def post_order(self):
        if self.left_child is not None:
            self.left_child.post_order()
        if self.right_child is not None:
            self.right_child.post_order()
        print(self.key)

    # 中序遍历
    def in_order(self):
        if self.left_child is not None:
            self.left_child.in_order()
        print(self.key)
        if self.right_child is not None:
            self.right_child.in_order()
