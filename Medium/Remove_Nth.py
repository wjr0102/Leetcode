# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        if count == 1:
            return None
        if count == n:
            return head.next
        node = head
        pos = count - n
        i = 1
        while i<pos:
            node = node.next
            i += 1
        node.next = node.next.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        # Del head
        if not fast:
            return head.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head