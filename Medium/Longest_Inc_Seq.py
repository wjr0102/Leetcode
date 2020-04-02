class Solution:
    '''
        动态规划：f为包含该元素的最长上升序列数
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        f = [1 for x in nums]
        n = len(nums)
        ans = 1
        for i in range(n):
            res = 1
            for j in range(i):
                if nums[i]>nums[j]:
                    res = f[j]+1
                    if res > f[i]:
                        f[i] = res
            if f[i]>ans:
                ans = f[i]
        return ans