# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        node1 = head
        node2 = head.next
        if not node2:
            return head
        ans = node2
        last_node = None
        while node1 and node2:
            # print(node1.val,node2.val)
            next_node = node2.next
            # 交换next
            node1.next = node2.next
            node2.next = node1
            # 与前面建立连接
            if last_node:
                last_node.next = node2
            last_node = node1
            node1 = next_node
            if node1:
                node2 = next_node.next
            
        return ans