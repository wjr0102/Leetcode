class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=2:
            return max(nums)
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = nums[1]
        res = max(dp[0],dp[1])
        for i in range(2,len(nums)):
            ans = -1
            for j in range(i-1):
                if dp[j]>ans:
                    ans = dp[j]
            dp[i] = ans + nums[i]
            if dp[i]>res:
                res = dp[i]
        # print(dp)
        return res

class Solution:
    def massage(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],dp[i-2]+ nums[i])
        # print(dp)
        return dp[-1]