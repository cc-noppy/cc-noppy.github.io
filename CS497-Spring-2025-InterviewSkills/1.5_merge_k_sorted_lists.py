from heapq import heappush, heappop

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val

def merge_k_sorted_lists(lists):
    min_heap = []
    
    for l in lists:
        if l:
            heappush(min_heap, l)

    dummy = ListNode(0)
    current = dummy

    while min_heap:
        smallest = heappop(min_heap)
        current.next = smallest
        current = current.next

        if smallest.next:
            heappush(min_heap, smallest.next)

    return dummy.next

def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
