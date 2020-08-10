'''
    696. 计数二进制字串
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
            先统计连续的字符串的长度，然后相邻的取最小值相加
        """
        last = s[0]
        counts = []
        count = 1
        res = 0
        for i in range(1,len(s)):
            if s[i]==last:
                count += 1
            else:
                counts.append(count)
                last = s[i]
                count = 1
        counts.append(count)
        for i in range(len(counts)-1):
            res += min(counts[i],counts[i+1])
        return res
