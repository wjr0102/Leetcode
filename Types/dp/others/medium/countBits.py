'''
    338. 比特位计数
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        """
            当已知i位二进制数时的1的个数的时候，对于i+1位数而言，只需要对应地加一即可，比如
                - 1010就是010再加上首位的1，即dp[10] = dp[10-8]+1
            
            current表示为当前轮次相差的位置
            nextnum表示下个轮次相差的位置
        """
        if num==0:
            return [0]
        dp = [0]*(num+1)
        dp[1] = 1
        current = 0
        nextnum = 2
        for i in range(2,num+1):
            if i==nextnum:
                current = nextnum
                nextnum = 2*nextnum
            dp[i] = dp[i-current] + 1
        return dp