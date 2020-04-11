import math
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # Find max c
        c = math.floor(math.sqrt(2*target))
        res = []
        for x in range(c,1,-1):
            if 2*target % x!=0:
                continue
            if (2*target//x+1-x) %2 !=0:
                continue
            a = (2*target//x+1-x)//2
            res.append([i for i in range(a,a+x)])

        return res