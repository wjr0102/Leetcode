class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        n = len(nums)
        # 能跳到的最大位置
        ans = nums[0]
        for i in range(1,n):
            # 最远能跳出n
            if ans>=(n-1):
                return True
            # 最远跳不到i<n
            if ans<i:
                return False
            ans = max(ans,i+nums[i])
        return False