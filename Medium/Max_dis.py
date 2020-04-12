class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        q = []
        dis = {}
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == 1:
                    q.append((i,j))
                    dis[(i,j)] = 0
                else:
                    dis[(i,j)] = -1
        if not q or (len(q))==len(grid)**2:
            return -1

        POS = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = -1
        flags = set()
        
        while q:
            land = q.pop(0)
            for pos in POS:
                if land[0]+pos[0]>=0 and land[0]+pos[0]<len(grid) and land[1]+pos[1]>=0 and land[1]+pos[1]<len(grid):
                    x = land[0]+pos[0]
                    y = land[1]+pos[1]
                    if grid[x][y]==0 and (x,y) not in flags:
                        flags.add((x,y))
                        if dis[x,y]>0:
                            dis[(x,y)] = min(dis[(x,y)],dis[land]+1)
                        else:
                            dis[x,y] = dis[land]+1
                        q.append((x,y))

        return dis[land]

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        dp = [[float("inf") for i in range(len(grid)+2)] for j in range(len(grid)+2)]
        for i in range(1,len(grid)+1):
            for j in range(1,len(grid)+1):
                if grid[i-1][j-1]==1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + 1
        res = -1

        for i in range(len(grid),0,-1):
            for j in range(len(grid),0,-1):
                if grid[i-1][j-1] == 0:
                    dp[i][j] = min(dp[i+1][j]+1,dp[i][j+1]+1,dp[i][j])
                    res = max(dp[i][j],res)

        if res==float("inf"):
            res = -1

        return res

