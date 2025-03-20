from collections import Counter
import heapq

def topKFrequent(nums, k):
    freq = Counter(nums)  
    return [x for x, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]
