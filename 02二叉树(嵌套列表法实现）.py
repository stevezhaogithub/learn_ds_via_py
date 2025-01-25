#
#  02二叉树(嵌套列表法实现）.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/25 16:15.
#


# 1. 通过嵌套列表法表示二叉树
btree = [
    'a',  # 根节点
    [
        'b',  # 左子树, 'b' 是左子树的根节点
        ['d', [], []],  # b 的左子树的根节点是 d, 且  d 是叶子节点，d 没有左右子树
        ['e', [], []]
    ],
    [
        'c',  # 右子树, 'c' 是右子树的根节点
        ['f', [], []],
        []
    ]
]


# 1. 构建一个数据项为 d 的, 左右子树都是空的二叉树
def binary_tree(d):
    return [d, [], []]


# 2. 插入左子树
def insert_left(root, lbranch):
    # 弹出原来的左子树, 索引为 1 表示原来的左子树
    t = root.pop(1)
    if len(t) > 1:  # 表示 t 节点除了数据项以外还有子节点（左右子树）, 每插入一个节点就有 3 项，哪怕这个节点只有 1 个数据也是三项['数据项本身', [], []]
        # 要插入左子树，所以insert()第一个参数是1，表示第二个元素
        root.insert(1, [lbranch, t, []])
    else:
        # 如果 len(t) == 0, 表示这个节点什么也没有。len(t) 要么等于0，要么等于3，所以只要判断 len(t) > 1就相当于判断节点 t 是否有子树了
        root.insert(1, [lbranch, [], []])
    return root


# 3. 插入右子树
def insert_right(root, rbranch):
    t = root.pop(2)
    if len(t) > 1:
        # 要插入右子树，所以 insert() 第一个参数是 2，表示第三个元素。每个节点有3个元素组成
        root.insert(2, [rbranch, [], t])
    else:
        root.insert(2, [rbranch, [], []])
    return root


# 4.
def get_root_value(root):
    return root[0]


#
def set_root_value(root, value):
    root[0] = value


#
def get_left_child(root):
    return root[1]


#
def get_right_child(root):
    return root[2]


if __name__ == '__main__':
    # 创建一个数据项为 3 的空的二叉树
    tree = binary_tree(3)  # [3, [], []]
    print(tree)

    # 插入一个左节点（数据项为 4 ）
    insert_left(tree, 4)
    print(tree)

    # 插入一个左节点（数据项为 5 ）
    insert_left(tree, 5)
    print(tree)

    # 插入一个右节点（数据项为 6 ）
    insert_right(tree, 6)
    print(tree)

    insert_right(tree, 7)
    print(tree)

    # 获取 tree 的左子树
    ltree = get_left_child(tree)
    print(ltree)

    # 获取 tree 的右子树
    rtree = get_right_child(tree)
    print(rtree)

    # 设置根节点 tree 的数据项为 1000
    set_root_value(tree, 1000)

    # 将 ltree 的根节点的数据项设置为 9
    set_root_value(ltree, 9)
    print(ltree)
    print(tree)

    # 在 tree 的左子树 ltree 插入左节点 11
    insert_left(ltree, 11)
    print(tree)

    rtree = get_right_child(tree)
    print(rtree)

    rtree = get_right_child(rtree)
    print(rtree)