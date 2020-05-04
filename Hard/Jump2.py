class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        # i现在考虑的位置，j能否到达的位置
        i,j = 0,1
        last = 0
        dp = [0] * len(nums)
        while j<len(nums):
            last = i + nums[i]
            while j<len(nums) and last >= j:
                dp[j] = dp[i] + 1
                j += 1
            i += 1
            # print(dp,i,j)
        return dp[-1]