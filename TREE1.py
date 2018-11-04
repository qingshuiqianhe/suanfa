#coding:utf-8
"""二叉数遍历"""


class SubtreeIndexError(ValueError):
    pass


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def preTraverse(root):
    '''
    前序遍历
    '''
    if root == None:
        return
    print(root.value)
    preTraverse(root.left)
    preTraverse(root.right)


def pre_deep_func2(root):
    a = []
    while a or root:
        while root:
            print root.value
            a.append(root)
            root = root.left
        h = a.pop()
        root = h.right


def midTraverse(root):
    '''
    中序遍历
    '''
    if root == None:
        return
    midTraverse(root.left)
    print(root.value)
    midTraverse(root.right)


def mid_deep_func2(root):
    a = []
    while a or root:
        while root:
            a.append(root)
            root = root.left
        h = a.pop()
        print h.value
        root = h.right


def afterTraverse(root):
    '''
    后序遍历
    '''
    if root == None:
        return
    afterTraverse(root.left)
    afterTraverse(root.right)
    print(root.value)


def after_deep_func2(root):
    a = []
    b = []
    while a or root:
        while root:
            b.append(root.value)
            a.append(root)
            root = root.right
        h = a.pop()
        root = h.left
    print b[::-1]


# 广度优先
def level_func(root):
    a = []
    a.append(root)
    while a:
        head = a.pop(0)
        print head.value
        if head.left:
            a.append(head.left)
        if head.right:
            a.append(head.right)


def get_tree(pre, mid):
    # 已知前序中序 还原
    if len(pre) == 0:
        return None
    if len(pre) == 1:
        return Node(pre[0])
    root = Node(pre[0])
    root_index = mid.index(pre[0])
    print pre[1:root_index + 1], mid[:root_index]
    root.left = get_tree(pre[1:root_index + 1], mid[:root_index])
    root.right = get_tree(pre[root_index + 1:], mid[root_index + 1:])
    return root


if __name__=='__main__':
    root = Node('D', Node('B', Node('A'), Node('C')), Node('E', right=Node('G', Node('F'))))
    print('前序遍历：')
    # preTraverse(root)
    # pre_deep_func2(root)
    # print('\n')
    print('中序遍历：')
    # midTraverse(root)
    # print('\n')
    # print('后序遍历：')
    # afterTraverse(root)
    # print('\n')

    head = get_tree([1, 2, 4, 5, 8, 9, 11, 3, 6, 7, 10], [4, 2, 8, 5, 11, 9, 1, 6, 3, 10, 7])
    pre_deep_func2(head)
