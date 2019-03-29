#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 20:21:06
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 20:35:00


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if not root:
        return 0
    nodes = [node]
    depths = [1]
    max_depth = 1
    while nodes:
        node = nodes.pop(0)
        depth = depths.pop(0)
        max_depth = max(depth, max_depth)
        if node.left:
            nodes.append(node.left)
            depths.append(depth + 1)
        if node.right:
            nodes.append(node.right)
            depths.append(depth + 1)

    return max_depth

    '''
        if not root: 
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
    '''
