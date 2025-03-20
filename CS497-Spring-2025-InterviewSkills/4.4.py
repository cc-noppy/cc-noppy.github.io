from collections import deque

def shortestSubarray(nums, k):
    prefix_sum = [0]
    for num in nums:
        prefix_sum.append(prefix_sum[-1] + num)
    
    dq = deque()
    min_len = float('inf')
    
    for i, curr_sum in enumerate(prefix_sum):
        while dq and curr_sum - prefix_sum[dq[0]] >= k:
            min_len = min(min_len, i - dq.popleft())
        while dq and prefix_sum[dq[-1]] >= curr_sum:
            dq.pop()
        dq.append(i)
    
    return min_len if min_len != float('inf') else -1