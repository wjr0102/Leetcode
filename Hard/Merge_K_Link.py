#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 17:57:14
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 18:04:39


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
