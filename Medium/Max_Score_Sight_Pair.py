''' 1014.
dp数组表示对于i以后的景点而言，它们的最优选择。
dp[i] = max(dp[i-1]-1,A[i]):
    - 要么是之前的最优选择-1
    - 要么就是选择自身。
优化为空间O(1)
'''
class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        last = A[0]
        res = 0
        for i in range(1,len(A)):
            res = max(res,A[i]+last-1) 
            last = max(last - 1,A[i])
        return res