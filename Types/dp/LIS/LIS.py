'''
    300. 最长上升子序列
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
            dp. O(n^2)
        """
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

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = [float(inf)]*len(nums)
        res = 0
        for num in nums:
            l,r = 0,res
            # print("num=%d"%num)
            while l<=r:
                m = (l+r)//2
                # print(l,r,m)
                if tail[m]<num:
                    l = m + 1
                else:
                    r = m - 1
            tail[l] = num
            if l==res:
                res += 1
        # print(tail)
        return res
