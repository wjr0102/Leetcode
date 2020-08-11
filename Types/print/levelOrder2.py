'''
    剑指offer 32-2 层遍历二叉树(分层)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        depth = 1
        res = []
        while q:
            level = []
            next_depth = 0
            for i in range(depth):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                    next_depth += 1
                if node.right:
                    q.append(node.right)
                    next_depth += 1
            res.append(level)
            depth = next_depth
        return res
