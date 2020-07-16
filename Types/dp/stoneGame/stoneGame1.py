'''
    877. 石子游戏

    dp通用解:
        dp[i][j]表示piels[i:j+1]下的最优分数
        那么对于先手f_dp:
            - 初始条件: 
                f_dp[i][i] = piels[i] (只有一堆石子)
            - 递推条件: 
                - 要么拿开始的(i)，剩下的对于其而言就是s_dp[i+1][j]
                - 要么拿最后一个(j)，剩下的就是s_dp[i][j-1]
                f_dp[i][j] = max(piels[i]+s_dp[i+1][j],piels[j]+s_dp[i][j-1])
        对于后手s_dp:
            - 初始条件:
                s_dp[i][i] = 0
            - 递推条件:
                - 如果先手拿了i, s_dp[i][j] = f_dp[i+1][j]
                - 否则, s_dp[i][j] = f_dp[i][j-1]

    由此可知，当其为偶数堆时，先手必胜
'''
import collections
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        f_dp = {}
        s_dp = {}
        n = len(piles)
        for i in range(n):
            f_dp[i] = collections.defaultdict(int)
            s_dp[i] = collections.defaultdict(int)
            f_dp[i][i] = piles[i]
        # 斜着填
        # 对角线已填，剩下n-1条斜线
        for a1 in range(1,n):
            # 这条对角线填(i,n)个空
            for a2 in range(n-a1):
                # print(a1,a2)
                i = a2
                j = a1 + a2
                # print(i,j)
                # 先手挑哪个 0: start 1: end
                pick = 0
                # 挑end大
                if s_dp[i+1][j]+piles[i]<s_dp[i][j-1]+piles[j]:
                    f_dp[i][j] = s_dp[i][j-1]+piles[j]
                    pick = 1
                else:
                    f_dp[i][j] = s_dp[i+1][j]+piles[i]
                if pick:
                    s_dp[i][j] = f_dp[i][j-1]
                else:
                    s_dp[i][j] = f_dp[i+1][j]
        # print(f_dp)
        # print(s_dp)
        if f_dp[0][n-1]>s_dp[0][n-1]:
            return True
        return False
