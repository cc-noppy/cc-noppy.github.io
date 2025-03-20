import heapq

def peekTopK(heap, k):
    if k > len(heap):
        return sorted(heap, reverse=True)
    
    result = []
    max_heap = [(-heap[0], 0)]  # Store negative values for max-heap behavior
    heapq.heapify(max_heap)
    
    while k > 0 and max_heap:
        val, idx = heapq.heappop(max_heap)
        result.append(-val)
        k -= 1
        
        left_child = 2 * idx + 1
        right_child = 2 * idx + 2
        
        if left_child < len(heap):
            heapq.heappush(max_heap, (-heap[left_child], left_child))
        if right_child < len(heap):
            heapq.heappush(max_heap, (-heap[right_child], right_child))
    
    return result