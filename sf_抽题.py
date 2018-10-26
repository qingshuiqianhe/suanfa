# coding:utf-8
import random

# 获取各种题目长度
a = [i for i in range(1, 100)]
b = [i for i in range(1, 50)]
c = [i for i in range(1, 500)]

"""随机数，设定一个难度系数，就是重复率，一次生成出五套，内部重复的有多少，
做题库的时候是不是要加个参数，试题的难度划分五档？？？。题目都变成字典了那就"""

# random_test = random.randint(1, len(a))
new_test = []
repeat = None


# 设置抽选题目的数量，采取随机数抽选，后期完善
def _getNum(num, type_TiMu):
    a_test = []
    for i in range(num):
        random_test = random.randint(1, len(type_TiMu))
        if random_test not in a_test:
            a_test.append(random_test)
    new_test.append(a_test)
    return a_test


# 多次抽取，实验辨别重复率
def test_repeat():
    for i in range(100):
        _getNum(10, a)

test_repeat()
print new_test

