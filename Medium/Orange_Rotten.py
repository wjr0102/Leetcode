class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        freshs = set()
        times = {}
        flags = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rottens.append((i,j))
                    times[(i,j)] = 0
                elif grid[i][j] == 1:
                    freshs.add((i,j))
        if not rottens:
            if freshs:
                return -1
            else:
                return 0

        POS = ((0,1),(0,-1),(1,0),(-1,0))
        orange = None
        while rottens:
            orange = rottens.pop(0)
            flags.add(orange)
            for pos in POS:
                x = orange[0] + pos[0]
                y = orange[1] + pos[1]
                if x>=0 and x<len(grid) and y>=0 and y < len(grid[0]):
                    if grid[x][y] == 1 and (x,y) not in flags:
                        times[(x,y)] = times[orange] + 1
                        flags.add((x,y))
                        rottens.append((x,y))
                        freshs.remove((x,y))
        
        if freshs:
            return -1

        return times[orange]
