#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-13 22:48:45
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-13 23:06:43

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    p = self.has_cycle(head)
    q = head
    if p:
        while p != q:
            p.next
            q.next
        return p
    return None


def has_cycle(self, head):
    fast = head
    slow = head
    pre = slow
    while fast and fast.next:
        pre = slow
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return fast
    return False
