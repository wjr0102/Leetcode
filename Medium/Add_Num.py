# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = l1
        num1 = []
        while node:
            num1.append(node.val)
            node = node.next
        node = l2 
        num2 = []
        while node:
            num2.append(node.val)
            node = node.next
        
        def add(num1,num2):
            # print(num1,num2)
            pos = len(num2)
            res = [0 for i in range(len(num1)+1)]
            for i in range(-1,-pos-1,-1):
                s = res[i] + num1[i] + num2[i]
                res[i] = s%10
                res[i-1] = s//10
            # print(res)
            for i in range(-pos-1,-len(res),-1):
                s = res[i] + num1[i]
                res[i] = s%10
                res[i-1] = s//10
            return res

        if len(num1) > len(num2):
            res = add(num1,num2)
        else:
            res = add(num2,num1)
        # print(res)
        
        s = 0
        if res[0]==0:
            s = 1
        ans = ListNode(res[s])
        node = ans
        for i in range(s+1,len(res)):
            node.next = ListNode(res[i])
            node = node.next
        return ans
            