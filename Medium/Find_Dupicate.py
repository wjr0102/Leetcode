class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
            建图：index i -> nums[i]
            先找到相遇点
            把慢指针移动到起点，各自走一步直到相遇:
                假设环长为L,起点到环口a,环口到相遇点b:
                    2(a+b) = a+b+kL
                    a = kL-b = (k-1)L + c
                即慢指针从起点走到环口时，快指针也从相遇点走到环口
        '''
        p1 = 0
        p2 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[nums[p2]]
            if p1 == p2:
                break
        p1 = 0
        while True:
            p1 = nums[p1]
            p2 = nums[p2]
            if p1 == p2:
                return p1