import heapq

def kthSmallestPrimeFraction(arr, k):
    min_heap = [(arr[i] / arr[-1], i, len(arr) - 1) for i in range(len(arr) - 1)]
    heapq.heapify(min_heap)
    
    for _ in range(k):
        val, i, j = heapq.heappop(min_heap)
        if j - 1 > i:
            heapq.heappush(min_heap, (arr[i] / arr[j - 1], i, j - 1))
    
    return [arr[i], arr[j]]