'''
    剑指offer42. 连续子数组的最大和
    面试题16.17
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in range(1,len(nums)):
            if dp[i-1]<0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1]+nums[i]
        return max(dp)