'''
    剑指offer 47. 礼物的最大价值
'''
class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        # 逆向dp
        # 下边界
        for j in range(m-2,-1,-1):
            grid[-1][j] += grid[-1][j+1]
        # 右边界
        for i in range(n-2,-1,-1):
            grid[i][-1] += grid[i+1][-1]
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                grid[i][j] += max(grid[i+1][j],grid[i][j+1])
        return grid[0][0]