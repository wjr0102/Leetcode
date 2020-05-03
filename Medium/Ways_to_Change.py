'''
    对硬币循环避免重复
'''
class Solution:
    def waysToChange(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        coins = (25,10,5,1)
        for coin in coins:
            for i in range(1,n+1):
                if i - coin >= 0:
                    dp[i] = (dp[i] + dp[i-coin]) % 1000000007
        return dp[n]

'''
    数学法
'''
class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]

        f = [1] + [0] * n
        for coin in coins:
            for i in range(coin, n + 1):
                f[i] += f[i - coin]
        return f[n] % mod
