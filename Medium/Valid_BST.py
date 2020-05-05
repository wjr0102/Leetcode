# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
    递归  
'''

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def isValid(node: TreeNode, val1: int, val2: int) -> bool:
            '''
                @parameters:
                    val1: 最右叶子结点
                    val2: 最左叶子结点
            '''
            if not node:
                return True
            if val1 < node.val and val2 > node.val:
                return isValid(node.left,val1,node.val) and isValid(node.right,node.val,val2)
            else:
                return False
        
        return isValid(root,float("-inf"),float("inf"))


'''
    中序
'''
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, inorder = [], float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # 如果中序遍历得到的节点的值小于等于前一个 inorder，说明不是二叉搜索树
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

            
        