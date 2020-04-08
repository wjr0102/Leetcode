# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fp = head
        sp = head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        return sp
