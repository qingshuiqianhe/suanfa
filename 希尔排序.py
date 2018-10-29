# coding:utf-8
def shellSort(nums):
    # 设定步长
    step = len(nums)/2
    while step > 0:
        for i in range(step, len(nums)):
            # 类似插入排序, 当前值与指定步长之前的值比较, 符合条件则交换位置
            while i >= step and nums[i-step] > nums[i]:
                nums[i], nums[i-step] = nums[i-step], nums[i]
                i -= step
        step = step/2
    return nums


if __name__ == '__main__':
    nums = [9, 3, 5, 8, 2, 7, 1]

    print shellSort(nums)
