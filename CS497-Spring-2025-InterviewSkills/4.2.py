import bisect

def findClosestElements(arr, k, x):
    left = bisect.bisect_left(arr, x) - 1
    right = left + 1
    
    while k > 0:
        if left < 0:
            right += 1
        elif right >= len(arr):
            left -= 1
        elif abs(arr[left] - x) <= abs(arr[right] - x):
            left -= 1
        else:
            right += 1
        k -= 1
    
    return arr[left+1:right]