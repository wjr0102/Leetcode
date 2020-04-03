class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        res = 0
        if_odd = False

        for c in s:
            if not dic.__contains__(c):
                dic[c] = 1
            else:
                dic[c] += 1
        for c in dic:
            if dic[c]%2==0:
                res += dic[c]
            else :
                res += dic[c] - 1
                if_odd = True
        if if_odd:
            res += 1
        return res