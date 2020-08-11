'''
    213. 打家劫舍（环）
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
            根据不同情况讨论，简化为打家劫舍1
                - 选第一个，不选最后一个
                - 选最后一个，不选第一个
                - 两个都不选
            进行精简：
                - 不选第一个
                - 不选第二个
        """
        if not nums:
            return 0
        if len(nums)<=3:
            return max(nums)

        # 选第一个
        l1 = 0
        l2 = nums[2]
        ans1 = l2
        for i in range(3,len(nums)-1):
            ans1 = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans1
        ans1 += nums[0]

        # 选最后一个
        l1 = 0
        l2 = nums[-3]
        ans2 = l2
        for i in range(len(nums)-4,0,-1):
            ans2 = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans2
        ans2 += nums[-1]

        # 两个都不选
        l1 = 0
        l2 = nums[1]
        ans3 = l2
        for i in range(2,len(nums)-1):
            ans3 = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans3

        print(ans1,ans2,ans3)

        return max(ans1,ans2,ans3)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)<=3:
            return max(nums)

        # 不选第一个
        l1 = 0
        l2 = nums[1]
        ans1 = l2
        for i in range(2,len(nums)):
            ans1 = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans1

        # 不选最后一个
        l1 = 0
        l2 = nums[0]
        ans3 = l2
        for i in range(1,len(nums)-1):
            ans3 = max(l2,l1+nums[i])
            l1 = l2
            l2 = ans3

        print(ans1,ans3)

        return max(ans1,ans3)