#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 18:01:01
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 17:49:32

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


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


def merge(l1, l2):

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
    result.next = merge(l1, l2)

    return result


def showList(l):
    print("----SHOW----")
    while l:
        print(l.val)
        l = l.next


if __name__ == "__main__":
    n = 2
    val1 = [-9, 3]
    list1 = []
    for i in range(n - 1, -1, -1):
        node = ListNode(val1[i])
        if i != n - 1:
            node.next = list1[n - i - 2]
        list1.append(node)
    m = 2
    val2 = [5, 7]
    list2 = []
    for i in range(m - 1, -1, -1):
        node = ListNode(val2[i])
        if i != n - 1:
            node.next = list2[m - i - 2]
        list2.append(node)
    l1 = list1[-1]
    l2 = list2[-1]
    result = merge(l1, l2)
    showList(result)
