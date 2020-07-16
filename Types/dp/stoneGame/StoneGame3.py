'''
    1406. 石子游戏3

    前123堆
'''
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        suffix = [0]*(n+1)
        for i in range(n-1,-1,-1):
            suffix[i] = suffix[i+1] + stoneValue[i]
        
        dp = [0]*n
        dp[n-1] = stoneValue[n-1]
        for i in range(n-2,-1,-1):
            if i==n-2:
                dp[i] = max(stoneValue[-1]+stoneValue[-2],stoneValue[-2])
            elif i==n-3:
                dp[i] = max(suffix[i]-dp[-2],suffix[i]-dp[-1],suffix[i])
            else:
                dp[i] = suffix[i] - min(dp[i+1:i+4])
        # print(suffix)
        # print(dp)
        if dp[0]>suffix[0]/2:
            return "Alice"
        elif dp[0]<suffix[0]/2:
            return "Bob"
        else:
            return "Tie"    
                