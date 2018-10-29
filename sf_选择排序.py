# coding:utf-8
# 直接选择排序算法
"""
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。
"""

# 1
def select_sort(lst):
    for i in range(len(lst)-1):  # 循环len(lst)-1 次
        k =i
        for j in range(i, len(lst)):  # k是已知最小元素位置
            if lst[k] > lst[j]:
                k = j
        if i != k:
            # lst[k] 是最小元素，检查是否交换
            lst[k], lst[i] = lst[i], lst[k]
    return lst


#  2
def select_sort2(lists):
    # 选择排序
    count = len(lists)
    for i in range(count):
        min = i
        for j in range(i + 1, count):
            if lists[min] > lists[j]:
                min = j
        lists[min], lists[i] = lists[i], lists[min]
    return lists


A = [5, 2, 4, 9, 3, 6, 8, 7]
a = select_sort(A)
b = select_sort2(A)
print(a, b)
