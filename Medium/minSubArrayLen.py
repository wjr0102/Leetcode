'''
    209. 长度最小的连续子数组
'''
class Solution:
    '''
        滑动窗口
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums)<s:
            return 0
        
        # 算左不算右
        l = 0
        r = 1
        res = float("inf")
        ans = nums[l]
        # 滑动窗口
        while r<len(nums):
            # 右指针往右滑
            while r<len(nums) and ans<s:
                ans += nums[r]
                r += 1
            # 左指针往右滑
            while l<r and ans-nums[l]>=s:
                ans -= nums[l]
                l += 1
            res = min(r-l,res)
            # print("l=%d,r=%d,ans=%d,res=%d"%(l,r,ans,res))
            # 左指针往右滑一格
            ans -= nums[l]
            l += 1
        return res

class Solution:
    '''
        前缀和+二分
    '''
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums or sum(nums)<s:
            return 0
        # 前缀和
        total = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            total[i] = nums[i-1] + total[i-1]
        print(total)

        def check(m):
            for i in range(m,len(nums)+1):
                beg = i-m
                a = total[i]-total[beg]
                if a>=s:
                    return True
            return False
        
        # 二分法
        l = 0
        r = len(nums)
        while l<=r:
            m = (l+r)//2
            # print(l,r,m)
            if check(m):
                if not check(m-1):
                    return m 
                r = m - 1
            else:
                l = m + 1
        return 0

