from collections import deque

def shortestSubarray(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)  # Prefix sum array, starting with 0

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    min_len = float('inf')
    dq = deque()

    for j in range(n + 1):
        while dq and prefix_sum[j] - prefix_sum[dq[0]] >= k:
            min_len = min(min_len, j - dq.popleft())

        while dq and prefix_sum[j] <= prefix_sum[dq[-1]]:
            dq.pop()

        dq.append(j)

    return min_len if min_len != float('inf') else -1