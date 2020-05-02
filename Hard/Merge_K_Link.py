#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 17:57:14
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2020-04-30 11:21:27

'''
    顺序
'''

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        
        MAX = float("inf")
        index = -1
        for i in range(len(lists)):
            if not lists[i]:
                continue
            if lists[i].val < MAX:
                MAX = lists[i].val
                index = i
        if index == -1:
            return None
        head = lists[index]

        for i in range(len(lists)):
            # print("%d th"%i)
            if i==index:
                continue
            p2 = lists[i]
            p1 = head
            while p1 and p2:
                # node = head
                # while node:
                #     print(node.val,end=",")
                #     node = node.next
                # print()
                while p1.next and p1.next.val < p2.val:
                    p1 = p1.next
                n1 = p1.next
                if n1:
                    # print("p1 = %d\tn1 = %d"%(p1.val,n1.val))
                    # 没有到头
                    last = p2
                    while p2 and p2.val<=n1.val:
                        p1.next = p2
                        p1 = p2
                        last = p2
                        p2 = p2.next
                    # if p2:
                    #     # l2没到头
                    #     print("p2 = %d\tlast = %d"%(p2.val,last.val))
                    # else:
                    #     # l2到头
                    #     print("The End!")
                    last.next = n1
                else:
                    # print("p1 = %d\t n1 the end!"%p1.val)
                    # 到头
                    p1.next = p2
                p1 = n1
                
        return head

'''
    分治
'''

def mergeKLists(lists):

    if len(lists) == 0:
        return None

    if len(lists) == 1:
        return lists[0]

    if len(lists) == 2:
        return mergeTwoLists(lists[0], lists[1])

    l1 = lists[:len(lists) // 2]
    l2 = lists[len(lists) // 2:]
    l1 = mergeKLists(l1)
    l2 = mergeKLists(l2)
    return mergeTwoLists(l1, l2)


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1

    result = ListNode(0)
    if l1.val < l2.val:
        result.val = l1.val
        l1 = l1.next
    else:
        result.val = l2.val
        l2 = l2.next

    node = result
    while l1 and l2:
        print(l1.val, l2.val)
        next_node = ListNode(0)
        if l1.val < l2.val:
            next_node.val = l1.val
            l1 = l1.next
        else:
            next_node.val = l2.val
            l2 = l2.next
        node.next = next_node
        node = node.next
        showList(result)

    while l1:
        node.next = l1
        node = node.next
        l1 = l1.next
    while l2:
        node.next = l2
        node = node.next
        l2 = l2.next

    return result

'''
    优先队列
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        q = PriorityQueue()
        head = ListNode(0)
        tail = head
        for l in lists:
            if l:
                q.put((l.val,id(l),l))
        while not q.empty():
            val, _, node = q.get()
            tail.next = node
            tail = node
            np = node.next
            if np:
                q.put((np.val,id(np),np))
        return head.next
