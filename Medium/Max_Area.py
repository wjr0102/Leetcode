class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        ans = 0
        move_left = True
        while l<r:
            if height[l]>height[r]:
                move_left = False
                h = height[r]
            else:
                h = height[l]
            res = h*(r-l)
            if res>ans:
                ans = res
            if move_left:
                l += 1
            else:
                r -= 1
                move_left = True
        return ans