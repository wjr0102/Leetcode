class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        last1 = float("inf")
        for i in range(len(nums)):
            if nums[i] == last1:
                continue
            a = nums[i]
            last1 = a
            last2 = float("inf")
            for j in range(i+1,len(nums)):
                if a + 3*nums[j] > target:
                    break
                if nums[j] == last2:
                    continue
                b = nums[j]
                last2 = b
                l = j + 1
                r = len(nums) - 1
                while l < r:
                    c = nums[l]
                    d = nums[r]
                    if a+b+c+d==target:
                        res.append([a,b,c,d])
                        while l<len(nums) and c==nums[l]:
                            l += 1
                        while r>j and d==nums[r]:
                            r -= 1
                    elif a+b+c+d<target:
                        while l<len(nums) and c==nums[l]:
                            l += 1
                    else:
                        while r>j and d==nums[r]:
                            r -= 1
        return res