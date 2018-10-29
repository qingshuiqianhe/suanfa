# coding:utf-8
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(1, len(lst)-i):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
    return lst


# 改进
def bubble_sort2(lst):
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst)-1):
            if lst[j-1] > lst[j]:
                lst[j-1], lst[j] = lst[j], lst[j-1]
                found = True
        if not found:
            break
    return lst


A = [5, 2, 4, 9, 3, 6, 8, 7]
a = bubble_sort(A)
b = bubble_sort2(A)
print(a, b)
