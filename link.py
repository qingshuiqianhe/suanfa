# coding:utf-8
"""python 链表操作"""


class LNode:
    """结点"""
    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = None


class LinkedListUnderflow(ValueError):
    pass


class List:
    """单链表"""

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def prepend(self, elem):
        self._head = LNode(elem, self._head)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow("in pop")
        e = self._head.elem
        self._head = self._head.next
        return e

    def append(self, x):
        if self._head is None:
            self._head = LNode(x)
            return
        p = self._head
        while p.next is not None:
            p = p.next
        p.next = LNode(x)

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow('in pop last')
        p = self._head
        if p.next is None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        return e

    def find(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                return p.elem
            p = p.next

    def printall(self):
        p = self._head
        while p is not None:
            print p.elem
            if p.next is not None:
                print ','
            p = p.next
        print ''

    def for_each(self, proc):
        p = self._head
        while p is not None:
            print p.elem
            p = p.next

    def elements(self):
        p = self._head
        while p is not None:
            yield p.elem
            p = p.next

    def filter(self, pred):
        p = self._head
        while p is not None:
            if pred(p.elem):
                yield p.elem
            p = p.next


class List1(List):
    """优化尾部插入"""
    def __init__(self):
        List.__init__(self)
        self._rear = None  # 尾结点引用域

    def prepend(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear = LNode(elem, self._head)

    def append(self, elem):
        if self._head is None:
            self._head = LNode(elem, self._head)
            self._rear = self._head
        else:
            self._rear.next = LNode(elem)
            self._rear = self._rear.next

    def pop(self):
        """
        空表
        只有一个元素
        到p.next 是最后的结点
        :return:
        """
        if self._head is None:
            return LinkedListUnderflow('link is none')
        p = self._head
        if p.next is not None:
            e = p.elem
            self._head = None
            return e
        while p.next.next is not None:
            p = p.next
        e = p.next.elem
        p.next = None
        self._rear = p
        return e


class LCLisr:
    """循环单链表"""
    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p.next = p
            self._rear = p
        else:
            p.next = self._rear.next
            self._rear.next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear.next

    def pop(self):
        if self._rear is None:
            raise LinkedListUnderflow('pop error in cllist')
        p = self._rear.next
        if self._rear is p:
            self._rear = p
        else:
            self._rear.next = p.next
        return p.elem

    def printall(self):
        if self.is_empty():
            return
        p = self._rear.next
        while 1:
            print p.elem
            if p is self._rear:
                break
            p = p.next


'''双链表'''


class DLnode(LNode):
    def __init__(self, elem, prev=None, _next=None):
        LNode.__init__(self, elem, _next)
        self.prev = prev


class DLList(List1):
    def __init__(self):
        List1.__init__(self)

    def prepend(self, elem):
        p = DLnode(elem, None, self._head)
        if self._head is None:
            self._rear = p
        else:
            p.next.prev = p
        self._head = p

    def append(self, elem):
        p = DLnode(elem, self._rear, None)
        if self._head is None:
            self._head = p
        else:
            p.prev.next = p
        self._rear = p

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('pop error in dllistt')
        e = self._head.elem
        self._head = self._head.next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_last(self):
        if self._head is None:
            raise LinkedListUnderflow("pop error in dllist")
        e = self._head.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear.next = None
        return e

    def rev(self):
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next
            q.next = p
            p = q
        self._head = p

    def sort1(self):
        if self._head is None:
            return
        # 从首节点开始处理
        crt = self._head.next

        while crt is not None:
            x = crt.elem
            p = self._head
            # 跳过小元素
            while p is not crt and p.elem <= x:
                p = p.next
            # 倒换大元素， 完成元素插入的工作
            while p is not crt:
                y = p.elem
                p.elem = x
                x = y
                p = p.next
            # 回添最后一个元素
            crt.elem = x
            crt = crt.next

    def sort(self):
        p = self._head
        if p is None or p.next is None:
            return
        rem = p.next
        p.next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p.next
            if q is None:
                self._head = rem
            else:
                q.next = rem
            q = rem
            rem = rem.next
            q.next = p


def list_sort(lst):
    for i in range(1, len(lst)):
        x = lst[i]
        j = i
        while j > 0 and lst[j-1] > x:
            lst[j] = lst[j-1]
            j -= 1
        lst[j] = x


"""循环双链表"""


class DLCirList(DLList):

    def is_empty(self):
        if self._head is None:
            return

    def append(self, elem):
        if self._head is None:
            self._head = DLnode(elem)
        p = self._head
        while self._head is not None:
            q = self._head.next
        q.next = DLnode(elem, q.next, p.next)

    def pop(self):
        if self._head is None:
            raise LinkedListUnderflow('error in dlclist pop')
        e = self._head.elem
        if self._head.next is None:
            return e
        prev = self._head.prev
        prev.next = self._head
        self._head.next = prev.elem

    def prepend(self, elem):
        if self._head is None:
            self._head = DLnode(elem)
        p = self._head
        while self._head is not None:
            q = self._head.next
        DLnode(elem, q, p)


"""josephus, 转圈报数出局问题"""


def josephus_A(n, k, m):
    people = list(range(2, n+1))
    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print people[i], ''
                people[i] = 0
            i = (i+1) % n
        if num < n -1:
            print ','
        else:
            print ''
    return


if __name__ == '__main__':
    ss = List1()
    ss.prepend(99)
    for i in range(11, 20):
        ss.append(i)

    for x in ss.filter(lambda y: y % 2 == 0):
        print x
    ss.find()










