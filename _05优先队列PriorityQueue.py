#
#  _05优先队列PriorityQueue.py
#  pythonProject4
#
#  Created by Z. Steve on 2025/1/26 10:47.
#


'''
    1. 优先队列出队比较简单，都是从队首出队，但入队比较复杂，因为要考虑优先级问题
    2. 用二叉堆 Binary Heap 实现优先队列。二叉堆可以将优先队列的入队和出队复杂度都保持在 O(log n)
    3. 堆次序 Heap Order
    4. 堆排序（二叉堆实现排序，复杂度 O( nlog n )
'''


class BinaryHeap:
    # 初始化
    def __init__(self):
        # 下标为 0 的元素无用
        self.heap_list = [0]
        # 表示当前 list 的大小
        self.size = 0

    # 上浮操作
    def perc_up(self, i):
        # 如果有父节点的话，此处为什么 i // 2，请思考二叉树性质
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                tNode = self.heap_list[i // 2]
                self.heap_list[i // 2] = self.heap_list[i]
                self.heap_list[i] = tNode
            i = i // 2

    # 下沉
    def perc_down(self, i):
        while i * 2 <= self.size:
            min_child_idx = self.min_child(i)
            if self.heap_list[i] > self.heap_list[min_child_idx]:
                tNode = self.heap_list[i]
                self.heap_list[i] = self.heap_list[min_child_idx]
                self.heap_list[min_child_idx] = tNode
            i = min_child_idx

    # 插入
    def insert_key(self, k):
        self.heap_list.append(k)
        self.size += 1
        # 新 key 上浮操作
        self.perc_up(self.size)

    # 返回较小的那个 child node 的序号
    def min_child(self, i):
        # 只有一个节点的话，那么这个节点就是较小的那个节点
        if i * 2 + 1 > self.size:
            return i * 2
        else:  # 表示有两个子节点，所以要判断哪个子节点是比较小的那个子节点
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    # 移除最小项
    def delete_min(self):
        # 1. 移走堆顶
        ret = self.heap_list[1]
        # 相当于把最后一个节点搬到堆顶
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        # 相当于把最后一个节点移除（就是原来的 current node ）
        self.heap_list.pop()
        # 下沉
        self.perc_down(1)
        return ret

    # 从无序表中生成二叉堆
    def build_binary_heap(self, alist: list):
        # 从最后节点的父节点开始，因为叶子节点无需下沉
        i = len(alist) // 2
        self.size = len(alist)
        self.heap_list = [0] + alist[:]
        print(len(self.heap_list), i)
        while i > 0:
            print(self.heap_list, i)
            self.perc_down(i)
            i -= 1
        print(self.heap_list, i)


class PriorityQueue:
    def __init__(self):
        pass
