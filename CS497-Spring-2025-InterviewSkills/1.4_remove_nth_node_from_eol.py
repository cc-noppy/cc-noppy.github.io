class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head) 
    slow, fast = dummy, dummy

    for _ in range(n + 1):
        fast = fast.next

    while fast:
        slow, fast = slow.next, fast.next

    slow.next = slow.next.next

    return dummy.next  # Return new head

# Helper function (list -> linked list)
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function (linked list -> list)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result