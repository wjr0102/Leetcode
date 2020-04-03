# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    对于每个node，找出以此为root的最长路径长度
'''
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        queue = [root]
        while queue:
            node = queue.pop()
            # Depth of left node + Depth of right node
            ans = self.depth(node.left)+self.depth(node.right)
            if ans > res:
                res = ans
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def depth(self,root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        dic = {root:1}
        dep = 1
        while queue:
            node = queue.pop()
            if dic[node]>dep:
                dep = dic[node]
            if node.left:
                queue.append(node.left)
                dic[node.left] = dic[node] + 1
            if node.right:
                queue.append(node.right)
                dic[node.right] = dic[node] + 1
        return dep
            