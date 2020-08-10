'''
    337. 打家劫舍3（二叉树）
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def rob(self, root: TreeNode) -> int:
        """
            对于一棵二叉树，可以从下到上进行遍历dp思考（这样无后效性）

            对于每一个节点记录一个选择此节点的最优值tl,和不选择此节点的最优值ignore
                - 如果选择此节点，则其左右儿子均不能选择，因此
                    tl[node]=ignore[node.left]+ignore[node.right]
                - 如果不选择此节点，则说明对其儿子的选择没有要求，因此只需要取最大值即可
                    ignore[node]=max(ignore[node.left],tl[node.left])+max(ignore[node.right],tl[node.right])
            *用节点在二叉树中的位置索引来进行遍历.
        """
        if not root:
            return 0
        # 找到节点对应的索引
        q = [root]
        tl = collections.defaultdict(int)
        tl[0] = root.val
        find = {root:0}
        while q:
            node = q.pop(0)
            if node.left:
                index = find[node]*2+1
                tl[index] = node.left.val
                find[node.left] = index
                q.append(node.left)
            if node.right:
                index = find[node]*2+2
                tl[index] = node.right.val
                find[node.right] = index
                q.append(node.right)
        # steal = [0]*len(tl)
        ignore = collections.defaultdict(int)
        keys = tl.keys()
        # 逆向dp
        for i in list(keys)[::-1]:
            l_child = i*2 + 1
            r_child = i*2 + 2
            # 偷parent
            tl[i] += ignore[l_child]+ignore[r_child]
            # 不偷parent
            ignore[i] = max(ignore[l_child],tl[l_child])+max(ignore[r_child],tl[r_child])
        return max(tl[0],ignore[0])