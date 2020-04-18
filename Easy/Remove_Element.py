class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        ans = len(nums) - nums.count(val)
        while l<r:
            while l<len(nums) and nums[l]!=val:
                l += 1
            while r>=0 and nums[r] == val:
                r -= 1
            if l<r and r>=0 and l<len(nums):
                nums[l] = nums[r]
                l += 1
                r -= 1
        return ans
                 