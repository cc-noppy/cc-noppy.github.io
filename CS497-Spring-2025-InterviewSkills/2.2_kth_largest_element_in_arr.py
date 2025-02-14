import random

def quickselect(nums, left, right, k):
    pivot_n = partition(nums, left, right)

    if pivot_n == k:
        return nums[pivot_n]
    elif pivot_n > k:
        return quickselect(nums, left, pivot_n - 1, k)
    else:
        return quickselect(nums, pivot_n + 1, right, k)

def partition(nums, left, right):
    pivot = nums[right]
    i = left
    for j in range(left, right):
        if nums[j] >= pivot: 
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = nums[right], nums[i]
    return i 

def find_kth_largest(nums, k):
    k_index = k - 1 
    return quickselect(nums, 0, len(nums) - 1, k_index)