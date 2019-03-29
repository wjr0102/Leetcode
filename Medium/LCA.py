#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-29 19:06:52
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-29 20:06:14

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
Binary Search Tree
'''


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    p_path = findAncestors(root, p)
    q_path = findAncestors(root, q)
    p_pointer = 0
    q_pointer = 0

    while (p_pointer + 1 < len(p_path) and q_pointer + 1 < len(q_path)):
        if (p_path[p_pointer].val - p_path[p_pointer + 1].val) * (q_path[q_pointer].val - q_path[q_pointer + 1].val) < 0:
            break
        else:
            p_pointer += 1
            q_pointer += 1

    return q_path[q_pointer]


def findAncestors(root, p):
    node = root
    path = []
    while node.val != p.val:
        path.append[node]
        if node.val > p.val:
            node = node.left
        else:
            node = node.right
    path.append(p)
    return path


'''
Binary Tree

考虑任一节点和pq的相对位置：
    1. 如果pq处于此节点的同一子树，则只有一棵子树有返回值，该子树将继续遍历
    2. 如果pq处于此节点的不同子树时，则两棵子树都有返回值，此节点为最近共同祖先
'''


def lowestCommonAncestor(root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root in (None, p, q):
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left and right:
        return root
    elif left:
        return left
    else:
        return right
