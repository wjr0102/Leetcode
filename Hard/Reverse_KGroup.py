# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        fast = head
        slow = head
        is_end = False
        is_found = False
        ans = None
        last_node = None
        while fast:
            # 找到这一组最后一个
            for i in range(k-1):
                if not fast.next:
                    is_end = True
                    break
                fast = fast.next
            # 不足k个
            if is_end:
                break
            # 确定ans
            if not is_found:
                ans = fast
                is_found = True

            # 连接（翻转后的）上一组的最后一个和这一组的第一个
            if last_node:
                last_node.next = fast
            # 下一组第一个
            fast = fast.next
            #print(slow.val,fast.val)
            # 翻转后的最后一个
            last_node = slow
            # 翻转
            next_node = fast
            while slow != fast:
                temp = slow.next
                slow.next = next_node
                next_node = slow
                slow = temp
            
        return ans
