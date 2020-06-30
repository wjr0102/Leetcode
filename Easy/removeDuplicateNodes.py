'''
    面试题02.01 移除重复节点

    不使用额外空间，则需要O(n^2)复杂度
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        flags = set()
        p1 = head
        p2 = head
        while p1:
            if p1.val in flags:
                p2.next = p1.next
            else:
                flags.add(p1.val)
                p2 = p1
            p1 = p1.next
        return head