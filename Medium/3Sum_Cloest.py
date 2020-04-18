class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float("inf")
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l<r:
                res = nums[l] + nums[r] + nums[i]
                if res < target:
                    l += 1
                else:
                    r -= 1
                if abs(target-res) < abs(target-ans):
                    ans = res
        return ans