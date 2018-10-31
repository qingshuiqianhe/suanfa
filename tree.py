#coding:utf-8
from stack_queue import *

# 二叉树数组实现


def BinTree(data, left=None, right=None):
    return [data, left, right]


def is_empty_BinTree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, data):
    btree[1] = data


def set_right(btree, data):
    btree[2] = data


t1 = BinTree(2, BinTree(4), BinTree(8))
print t1


# 优先队列

class PrioQueueError(ValueError):
    pass


class PrioQue:
    def __int__(self, elist=[]):
        self._elems = list(elist)
        self._elems.sort(reverse=True)

    def enqueue(self, e):
        i = len(self._elems) - 1
        while i >= 0:
            if self._elems[i] <= e:
                i -= 1
            else:
                break
        self._elems.insert(i+1, e)

    def is_empty(self):
        return not self._elems

    def peek(self):
        if self.is_empty():
            raise PrioQueueError('error in peek empey')
        return self._elems[-1]

    def dequeue(self):
        if self.is_empty():
            raise PrioQueueError('error in pop empey')
        return self._elems.pop()


class BinTNode:
    def __int__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def count_BinTNodes(t):
    if t is None:
        return 0
    else:
        return 1 + count_BinTNodes(t.left) + count_BinTNodes(t.right)


def sum_BinTNode(t):
    if t is None:
        return 0
    else:
        return t.data + sum_BinTNode(t.left) + sum_BinTNode(t.right)


def preorder(t, proc):
    """前序，中序，后序，改变顺序"""
    if t is None:
        return
    proc(t.data)
    preorder(t.left)
    preorder(t.right)


def levelorder(t, proc):
    """宽度优先"""
    qu = SQueue()
    qu.enqueue(t)
    while not qu.is_empty():
        n = qu.dequeue()
        if t is None:
            continue
        qu.enqueue(t.left)
        qu.enqueue(t.right)
        proc(t.data)


def preorder_nonrec(t, proc):
    s = Sstack()
    while t is not None or not s.is_empty():
        while t is not None:
            proc(t.data)
            s.push(t.right)
            t = t.left
        t = s.pop()


class HTNode(BinTNode):
    def __lt__(self, othernode):
        return self.data < othernode.data


class HuffmanPrioQ(PrioQue):
    def number(self):
        return len(self._elems)

def HuffmanTree(weights):
    trees = HuffmanPrioQ()
    for w in weights:
        trees.enqueue(HTNode(w))
    while trees.number() > 1:
        t1 = trees.dequeue()
        t2 = trees.dequeue()
        x = t1.data + t2.data
        trees.enqueue(HTNode(x, t1, t2))
    return trees.dequeue()
