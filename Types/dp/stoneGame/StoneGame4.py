'''
    1510. 石子游戏4

    取平方和
'''
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False]*(n+1)
        flags = set()
        for i in range(1,n+1):
            if ceil(math.sqrt(i))**2 == i:
                dp[i] = True
                flags.add(i)
            else:
                is_ok = True
                for before in flags:
                    is_ok = is_ok and dp[i-before]
                if is_ok:
                    dp[i] = False
                else:
                    dp[i] = True
        # print(dp)
        return dp[-1]