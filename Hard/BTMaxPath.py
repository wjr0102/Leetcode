#!/usr/local/bin
# -*- coding: utf-8 -*-
# @Author: Jingrou Wu
# @Date:   2019-03-28 14:32:53
# @Last Modified by:   Jingrou Wu
# @Last Modified time: 2019-03-28 15:11:34

# 递归
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = float('-inf')
        self.getMax(root)
        return self.ans
        
    def getMax(self,node):
        if node:
            left = max(0,self.getMax(node.left))
            right = max(0,self.getMax(node.right))
            self.ans = max(self.ans,node.val+left+right)
            return max(left,right)+node.val
        else:
            return 0

'''dp
f[node]=max()
'''