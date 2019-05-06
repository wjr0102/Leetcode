#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-13 23:20:40
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-13 23:35:05

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return None

        if not head or not head.next:
            return head

        if not head.next.next:
            if k % 2 == 0:
                return head
            else:
                head.next = head
                head.next = None
                head = head.next
            return head

        count = 0
        node = head
        while node:
            node = node.next
            count += 1

        for i in range(k % count):
            node = head
            while node.next.next:
                node = node.next
            node.next.next = head
            head = node.next
            node.next = None

        return head
