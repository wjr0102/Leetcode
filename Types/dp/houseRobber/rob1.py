'''
    198. 打家劫舍(相邻房子)
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        """
        if not nums:
            return 0
        l1 = 0
        l2 = nums[0]
        ans = l2
        for i in range(1,len(nums)):
            ans = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans
        #print(dp)
        return ans