# class Solution:
#     def superEggDrop(self, K: int, N: int) -> int:
#         if K==1:
#             return N
#         if N==1:
#             return 1

#         dp = [[0 for i in range(N)] for j in range(K)]
#         for i in range(N):
#             dp[0][i] = i+1
#         for i in range(K):
#             dp[i][0] = 1
#         print(dp)

#         for i in range(1,K):
#             y1 = -1
#             y2 = -1
#             for j in range(1,N):
#                 # Move y1
#                 if y2==-1:
#                     a1 = 1 + max(dp[i-1][y1+1],0)
#                 else:
#                     a1 = 1 + max(dp[i-1][y1+1],dp[i][y2])
#                 # Move y2
#                 if y1==-1:
#                     a2 = 1 + max(0,dp[i-1][y2+1])
#                 else:
#                     a2 = 1 + max(dp[i-1][y1],dp[i][y2+1])
#                 if a1 > a2:
#                     y2 += 1
#                     dp[i][j] = a2
#                 else:
#                     y1 += 1
#                     dp[i][j] = a1
#         print(dp)
#         print(dp[-1][-1])
#         return dp[-1][-1]

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        if K==1:
            return N
        if N==1:
            return 1

        dp = [[0 for i in range(N)] for j in range(2)]
        for i in range(N):
            dp[0][i] = i+1
        dp[1][0] = 1
        cur = 1
        last = 0
        for i in range(1,K):
            y1 = -1
            y2 = -1
            #print(i,cur,last)
            for j in range(1,N):
                # Move y1
                if y2==-1:
                    a1 = 1 + max(dp[last][y1+1],0)
                else:
                    a1 = 1 + max(dp[last][y1+1],dp[cur][y2])
                # Move y2
                if y1==-1:
                    a2 = 1 + max(0,dp[cur][y2+1])
                else:
                    a2 = 1 + max(dp[last][y1],dp[cur][y2+1])
                if a1 > a2:
                    y2 += 1
                    dp[cur][j] = a2
                else:
                    y1 += 1
                    dp[cur][j] = a1
            cur = 1-cur
            last = 1-last
        # print(dp)

        return dp[1-cur][-1]

if __name__ == "__main__":
    s = Solution()
    k = 2
    n = 7
    s.superEggDrop(k,n)