#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-04 19:55:09
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-10 14:06:57

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def sortList(self, head):
    """
    :type head: ListNode
    :rtype: ListNode
    """

    # 找中点
    if not head or not head.next:
        return head
    return self.mergeSort(head)


def mergeSort(self, head):
    if not head.next:
        return head
    qp, sp = head, head
    pre = None
    while qp and qp.next:
        pre = sp
        sp = sp.next
        qp = qp.next.next
    pre.next = None
    left = self.mergeSort(head)
    right = self.mergeSort(sp)
    return self.merge(left, right)


def merge(self, left, right):
    if not left:
        return right
    if not right:
        return left
    if left.val < right.val:
        res = left
        res.next = self.merge(left.next, right)
    else:
        res = right
        res.next = self.merge(left, right.next)
    return res
