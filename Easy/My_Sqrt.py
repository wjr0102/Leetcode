'''
    二分
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        l = 0
        r = x
        mid = (l+r)//2
        while True:
            if mid**2 > x:
                r = mid
            else:
                if (mid+1)**2 > x:
                    return mid
                l = mid
            mid = (l+r)//2

'''
    牛顿法
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
            Solve f(a) = a^2 - x = 0
            f'(a) = 2a
            Line: y - (a^2-x) = 2a(x-a)
            x = (x - a^2)/2a + a = x/2a + a/2
        '''
        if x == 1:
            return 1
        mid = x //2
        while not (mid**2<=x and (mid+1)**2>x):
            mid = (x//mid + mid)//2
            
        return mid