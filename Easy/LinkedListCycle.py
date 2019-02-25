def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow = head
    fast = head.next
    while (slow != fast):
        if (fast is None or fast.next is None):
            return False
        slow = slow.next
        fast = fast.next.next
        
    return true
