# coding:utf-8

"""
算法导论第三版 插入排序python实现，原书p10.
2017.8.20
by：清水谦和
"""

A = [5, 2, 4, 6, 1, 3]
print('A=', A)
# Python 索引问题，从0开始计数，范围（1，len（a））
for j in range(1, len(A)):
    key = A[j]
    print('KEY=', key)
    i = j-1
    # i>=0 ,不写‘=0’，无法对5进行排序
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i -= 1
    A[i+1] = key
    print('NEW A =', A)


'''
练习：
2.降序排列: 只需要改大于号为小于号即可
'''
A = [10, 5, 9, 6, 1, 3]
print('A=', A)
# Python 索引问题，从0开始计数，范围（1，len（a））
for j in range(1, len(A)):
    key = A[j]
    print('KEY=', key)
    i = j - 1
    # i>=0 ,不写‘=0’，无法对5进行排序
    while i >= 0 and A[i] < key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key
    print('NEW A =', A)
