#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 21:37:37
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 21:50:59


def getIntersectionNode(self, headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    lenA = 0
    lenB = 0

    node = headA
    while node:
        lenA += 1
        node = node.next

    node = headB
    while node:
        lenB += 1
        node = node.next

    # Assume A has longer length
    if lenA < lenB:

        temp = headB
        headB = headA
        headA = temp

        temp = lenB
        lenB = lenA
        lenA = temp

    for i in range(lenA - lenB):
        headA = headA.next

    while headA:
        if headA == headB:
            return headA
        else:
            headA = headA.next
            headB = headB.next

    return None
