'''
    因为有正负，所以保存最大和最小值
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        fmin,fmax,ans = nums[0],nums[0],nums[0]
        for i in range(1,len(nums)):
            a = min(fmin*nums[i],fmax*nums[i],nums[i])
            b = max(fmax*nums[i],fmin*nums[i],nums[i])
            ans = max(ans,a,b)
            fmin = a
            fmax = b
        return ans