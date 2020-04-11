import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        m = float("inf")
        dic = {}
        for x in deck:
            if dic.__contains__(x):
                dic[x] += 1
            else:
                dic[x] = 1
        for x in dic:
            if dic[x]<m:
                m = dic[x]

        print(m)
        if m == 1:
            return False

        def factor(a):
            res = []
            for i in range(1,(int)(math.sqrt(a))+1):
                if a % i == 0:
                    res.append(i)
                    res.append(a//i)
            res.remove(1)
            return res

        factors = factor(m)
        print(factors)
        
        for x in factors:
            count = 0
            for num in dic:
                if dic[num]%x!=0:
                    break
                else:
                    count += 1
            if count == len(dic):
                return True

        return False