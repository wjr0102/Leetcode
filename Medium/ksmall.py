#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-04-04 19:39:59
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-04-12 14:14:17

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthSmallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    index = findIndex(root)
    if index == k:
        return root
    if index < k:
        return kthSmallest(root.right, k - index)
    else:
        return kthSmallest(root.left, k)


def findIndex(node):
    nodes = [node]
    index = 1
    while nodes:
        n = nodes.pop(0)
        if n.left:
            nodes.append(n.left)
            index += 1
        if n.right and n != node:
            nodes.append(n.right)
            index += 1
    return index
