class Solution:
    def maxAreaOfIsland(self, grid):
        # Find all 1
        islands = []
        res = 0
        for i in range(len(grid)):
            print(grid[i])
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    islands.append((i,j))
        flags = set()
        POS = [(-1,0),(0,-1),(1,0),(0,1)]
        print(islands)
        for island in islands:
            if island not in flags:
                flags.add(island)
            else:
                continue
            queue = [island]
            ans = 0
            print(island)
            while queue:
                land = queue.pop()
                ans += 1
                for pos in POS:
                    newland_x = land[0]+pos[0]
                    newland_y = land[1]+pos[1]
                    if newland_x>=0 and newland_x<len(grid) and newland_y>=0 and newland_y<len(grid[0]):
                        if grid[newland_x][newland_y]==1 and (newland_x,newland_y) not in flags:
                            queue.append((newland_x,newland_y))
                            flags.add((newland_x,newland_y))
            if ans>res:
                res = ans

        return res

if __name__ == "__main__":
    s = Solution()
    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    print(s.maxAreaOfIsland(grid))
