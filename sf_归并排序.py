# coding:utf-8
import random
"""归并排序：关键操作是合并两个以排序的数组
假设 A[p,q], A[q+1,r]，只需要取两个数组开头较小的元素，对应数组移除该元素后，刷新，在取最小的元素，直到一个数组为空、
为了避免每个步骤检查数组是否为空，在数组最后添加一个‘哨兵（正无 穷大符号），当暴露哨兵时，把另外一个数组剩余元素逐个
添加
pop 的相对来说简单些， 思路不难，看个人想法和实现注意点"""


def ConfiationAlgorithm(str):
    if len(str) <= 1:   # 子序列
        return str
    mid = (len(str) / 2)
    left = ConfiationAlgorithm(str[:mid])  # 递归的切片操作
    right = ConfiationAlgorithm(str[mid:len(str)])
    result = []

    while len(left) > 0 and len(right) > 0:
        if ( left[0] <= right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if ( len(left) > 0 ):
        result.extend(ConfiationAlgorithm(left))
    else:
        result.extend(ConfiationAlgorithm(right))
    return result


if __name__ == '__main__':
    a = [20, 30, 64, 16, 8, 10, 99, 24, 75, 100, 69]
    print ConfiationAlgorithm(a)
    b = [random.randint(1, 1000) for i in range(10)]
    print ConfiationAlgorithm(b)

