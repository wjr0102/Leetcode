class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for i in range(num_people)]
        cur = 1
        sum_can = 0
        i = 0
        while sum_can<candies:
            cur = min(cur,candies-sum_can)
            res[i] += cur
            sum_can += cur
            cur += 1
            i += 1
            if i==num_people:
                i = 0
        return res

import math
class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        a = math.sqrt(2*candies)
        l = math.floor(a)   # 发完
        r = math.ceil(a)    # 没发完
        if r==l:
            r+= 1
        while l*r >= candies*2:
            l -= 1
            r -= 1
        res = [0 for i in range(num_people)]
        turn = l//num_people
        base1 = turn*(turn+1)//2
        base2 = (turn-1)*turn//2
        last = r%num_people - 1
        if last==-1:
            last = num_people - 1
        print(l,r,last,turn,base1,base2)
        for i in range(num_people):
            if i<last:
                res[i] = base1*num_people + (turn+1)*(i+1)
            elif i==last:
                res[i] = base2*num_people + turn*(i+1) + (candies-l*r//2)
            else:
                res[i] = base2*num_people + turn*(i+1)
        return res