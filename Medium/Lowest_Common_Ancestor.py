'''
    保存父节点信息
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {root:root}
        queue = [root]
        flags = set()
        # 记录父节点信息
        while queue:
            node = queue.pop()
            if node.left:
                parents[node.left] = node
                queue.append(node.left)
            if node.right:
                parents[node.right] = node
                queue.append(node.right)
        # 从p开始
        node = p
        while node != root:
            flags.add(node)
            node = parents[node]
        # 再从q开始
        node = q 
        while node != root:
            if node in flags:
                return node
            node = parents[node]
        return root
        
'''
    递归
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root in (None,p,q):
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
            

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def inSubTree(parent : 'TreeNode', child: 'TreeNode'):
            q = [parent]
            while q:
                node = q.pop()
                if node == child:
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            return False

        if inSubTree(p,q):
            return p
        if inSubTree(q,p):
            return q
        
        queue = [root]
        ans = None
        while queue:
            node = queue.pop(0)
            if inSubTree(node,p) and inSubTree(node,q):
                ans = node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return ans