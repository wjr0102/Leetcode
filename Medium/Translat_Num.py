'''
面试题46
'''
class Solution:
    '''
        递归
    '''
    def tn(self,num: int) -> int:
        # print(num)
        if num < 10:
            return 1
        if num>=10 and num < 26:
            return 2
        if num >= 26 and num<100:
            return 1
        s = str(num)
        n1 = int(s[0])
        n11 = int(s[1:])
        n2 = int(s[:2])
        n22 = int(s[2:])
        # print("n1=%d\tn11=%d\nn2=%d\tn22=%d"%(n1,n11,n2,n22))
        res = self.tn(n11)
        if n2 < 26:
            res += self.tn(n22)
        # print("res=%d"%res)
        return res
    
    def translateNum(self, num: int) -> int:
        return self.tn(num)

class Solution:
    '''
        带记忆的递归
    '''
    def __init__(self):
        self.strings = {}

    def tn(self,num: int) -> int:
        # print(num)
        if num < 10:
            return 1
        if num>=10 and num < 26:
            return 2
        if num >= 26 and num<100:
            return 1
        s = str(num)
        n1 = int(s[0])
        n11 = int(s[1:])
        n2 = int(s[:2])
        n22 = int(s[2:])
        # print("n1=%d\tn11=%d\nn2=%d\tn22=%d"%(n1,n11,n2,n22))
        if not self.strings.__contains__(n11):
            self.strings[n11] = self.tn(n11)
        res = self.strings[n11]
        if n2 < 26:
            if not self.strings.__contains__(n22):
                self.strings[n22] = self.tn(n22)
            res += self.strings[n22]
        # print("res=%d"%res)
        return res
    
    def translateNum(self, num: int) -> int:
        return self.tn(num)
            
class Solution:
    '''
        dp: 
        如果算上自己和前一个可以拼两个则:
            - dp[i] = dp[i-1] + dp[i-2]
        否则:
            - dp[i] = dp[i-1] 
    '''
    def translateNum(self, num: int) -> int:
        s = str(num)
        l1 = 1
        l2 = 1
        for i in range(len(s)-1):
            # print(l1,l2)
            a = int(s[i:i+2])
            if a>25 or a<10:
                l1 = l2
            else:
                temp = l2
                l2 = l1 + l2
                l1 = temp
        # print(dp)
        return l2
            