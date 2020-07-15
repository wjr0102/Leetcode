'''
    96. 不同的二叉搜索树
'''
class Solution:
    def numTrees(self, n: int) -> int:
        """
            n个结点中，一个为根结点，剩余的结点可能在左子树上也可能在右子树上，对于两颗子树的结点数进行遍历即可得到答案.。

            递推式: $dp[n] = sum _{i=0}^{n-1} dp[i]*dp[n-1-i]$
        """
        dp = [0]*(n+1)
        dp[0] = dp[1] = 1
        for i in range(2,n+1):
            # 左边几个节点
            for j in range(i):
                dp[i] += dp[j]*dp[i-j-1]
        return dp[n]

class Solution(object):
    def numTrees(self, n):
        """
            catalan数，由上述递推式得到
        """
        C = 1
        for i in range(0, n):
            C = C * 2*(2*i+1)/(i+2)
        return int(C)
