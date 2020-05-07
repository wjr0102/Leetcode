# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def isSame(a: TreeNode, b: TreeNode):
            if a and (not b):
                return False
            if (not a) and b:
                return False
            if (not a) and (not b):
                return True
            # print(a.val,b.val)
            if a.val == b.val:
                return isSame(a.left,b.left) and isSame(a.right,b.right)
            else:
                return False
        
        q = [s]
        while q:
            node = q.pop()
            if isSame(node,t):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
            