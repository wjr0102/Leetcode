#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 20:43:58
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 21:03:30


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return None
    stack = []
    node = head
    while node:
        stack.append(node)
        node = node.next
    new_head = stack.pop()
    node = new_head
    while stack:
        node.next = stack[-1]
        node = stack.pop()
    node.next = None

    return new_head


def reverseList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if not (head and head.next):
        return head

    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None

    return new_head
