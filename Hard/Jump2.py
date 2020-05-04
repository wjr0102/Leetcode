'''
    dp
'''
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

'''
    Greedy: Choose the postion which can cover largest range
'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        i = 0
        index = 1
        res = 0
        while i<len(nums) - 1:
            pos = i + nums[i]
            if pos >= len(nums)-1:
                res += 1
                return res
            res += 1
            # 选能跳得最远的位置
            for j in range(i+1,i+nums[i]+1):
                if j+nums[j]>pos:
                    pos = j+nums[j]
                    index = j
            i = index
        return res
