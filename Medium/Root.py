class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        paths = [(0,0)]
        curx = 0
        cury = 0
        for c in command:
            if c=="U":
                cury += 1
            else:
                curx += 1
            paths.append((curx,cury))

        # print("origin: %d,%d"%(x,y))
        # print(curx,cury)
        num = min(x // curx,y//cury)
        x = x - num*curx
        y = y - num*cury
        if (x,y) not in paths:
            return False
        index = paths.index((x,y))
        # print(index)

        for o in obstacles:
            n = min(o[0] // curx,o[1]//cury)
            o[0] = o[0] - n*curx
            o[1] = o[1] - n*cury
            if (o[0],o[1]) in paths:
                if n<num:
                    return False
                elif n==num and paths.index((o[0],o[1]))<index:
                    return False
        
        return True
