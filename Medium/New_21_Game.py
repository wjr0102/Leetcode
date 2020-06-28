'''
    837
'''
class Solution:
    '''
        dp[i]表示分数为i时的概率, 
        dp[i] = (1/w) * sum _{k=i-W-1}^{k=i-1}dp[k],
        即i的分数可由i-1,i-2,...,i-W-1得到

        又因为i不可能为负数，所以Ka=max(0,i-W-1)
        又因为当i>=k时，就不能再抽牌了，所以Kb=min(i-1,k-1)

        用total表示[Ka,Kb]的窗口和
    '''
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K==0:
            return 1
        if N==0:
            return 0
        dp = [1] * (N+1)
        dp[0] = 1
        dp[1] = 1/W
        # 窗口[i-W-1,i-1]和
        total = 1
        l = 0
        r = 1
        for i in range(2,N+1):
            if i-W-1 >= 0:
                total -= dp[i-W-1]
            if i - 1 < K:
                total += dp[i-1]
            dp[i] = total/W
        res = 0
        for i in range(K,N+1):
            res += dp[i]
        return res

class Solution:
    '''
        dp[i]表示得分为i时，成功的概率。所以结果为dp[0]
    '''
    def new21Game(self, N: int, K: int, W: int) -> float:
        if K==0:
            return 1
        if N==0:
            return 0
        dp = [1] * (N+1)
        total = min(N,K+W-1)-K
        for x in range(K-1,-1,-1):
            if x+W+1 <= N:
                total -= dp[x+W+1]
            total += dp[x+1]
            dp[x] = total/W
        return dp[0]