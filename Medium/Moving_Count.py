class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        queue = [(0,0)]
        flags = set()
        flags.add((0,0))
        POS = ((-1,0),(0,-1),(1,0),(0,1))
        while queue:
            pos = queue.pop()
            for p in POS:
                x = pos[0]+p[0]
                y = pos[1]+p[1]
                if (x,y) not in flags and x>=0 and x<m and y>=0 and y<n and self.cal(x,y)<=k:
                    queue.append((x,y))
                    flags.add((x,y))
        return len(flags)

    def cal(self,x:int,y:int)->int:
        x1 = x // 10
        x2 = x % 10
        y1 = y // 10
        y2 = y % 10
        return x1+x2+y1+y2