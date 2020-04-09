class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            last = -1
            for j in range(len(grid)):
                v = grid[i][j]
                if v==0:
                    last = v
                    continue
                if last>0:
                    ans -= min(v,last)*2
                ans += 6*v - 2*(v-1)
                last = v
                if i+1<len(grid):
                    row = grid[i+1][j]
                    ans -= min(row,v)*2
                # print(ans)
        return ans
            