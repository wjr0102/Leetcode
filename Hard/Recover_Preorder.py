# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def find_value(index):
            '''
                找到数字

                @Args:
                    index: 从第几个位置开始找
                
                @Returns:
                    index: 下一次从哪个位置开始找
                    num: 这次找到的数字
            '''
            num = ""
            while index < len(S) and S[index]!="-":
                num += S[index]
                index += 1
            return index,int(num)

        # 找到root的值
        i,num = find_value(0)
        root = TreeNode(num)
        # 层数
        level = 0
        # 层数字典
        depths = {0:root}
        while i < len(S):
            if S[i] == "-":
                level += 1
                i += 1
            else:
                # find value
                i,num = find_value(i)
                node = TreeNode(num)
                parent = depths[level-1]
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
                # 更新层数字典
                depths[level] = node
                level = 0
        return root