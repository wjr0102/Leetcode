class Solution:
    def fraction(self, cont: List[int]) -> List[int]:
        m = cont[-1]
        n = 1
        for i in range(len(cont)-1,0,-1):
            last = m
            m = cont[i-1]*m+n
            n = last
            #print(n,m)
        
        # def gcd(a,b):
        #     # a<b
        #     if a==0:
        #         return b
        #     return gcd(b%a,a)
        # if n > m:
        #     x = gcd(m,n)
        # else:
        #     x = gcd(n,m)
        return [m,n]