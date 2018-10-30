#coding:utf-8


class StackUnderflow(ValueError):
    pass


class LNode:
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = None


class Sstack():

    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def top(self):
        if self.elems == []:
            raise  StackUnderflow('TOP error in top')
        return self.elems[-1]

    def push(self, elem):
        self.elems.append(elem)

    def pop(self):
        if self.elems == []:
            raise StackUnderflow('error in pop')
        return self.elems.pop()


class LStack():
    # 基于链表技术实现的栈类， 用lnode做结点

    def __int__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderflow('ERROR IN lstack top')
        return self._top.elem

    def push(self, elem):
        self._top = LNode(elem, self._top)

    def pop(self):
        if self._top is None:
            raise StackUnderflow('error in lstack pop')
        p = self._top
        self._top = p.next
        return p.elem


def match_parents(s):
    ls = []
    parents = "()[]{}"
    open_parents = "([{"

    for i in range(len(s)):
        si = s[i]
        if parents.find(si) == -1:
            continue
        if si in open_parents:
            ls.append(si)
            continue
        if len(ls) == 0:
            return False
        p = ls.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False
    if len(ls) > 0:
        return False
    else:
        return True


class SQueue():
    def __int__(self, init_len = 8):
        self._len = init_len
        self._elems = [0]*init_len
        self._head = 0
        self._num = 0

    def is_empty(self):
        return self._num == 0

    def peek(self):
        if self._num == 0:
            return 'error in queue peek'
        return self._elems[self._head]

    def dequeue(self):
        if self._num == 0:
            return 'error in queue dequeue'
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1
        return e

    def enqueue(self, e):
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        old_len = self._len
        self._len *= 2
        new_elems = [0]*self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head +i) % old_len]
        self._elems, self._head = new_elems, 0





if __name__ == '__main__':
    test = '{[(])]}'
    print match_parents(test)





