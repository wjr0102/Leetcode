'''
    44. 通配符匹配
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
            dp[i][j]表示为长度为i的字符串s是否能和长度为j的模式字符p匹配

            -如果p[j]=="*":
                - 不使用这个"*"（即"*"匹配为空字符串）
                    dp[i][j] = dp[i][j-1]
                - 使用此"*":
                    - 此"*"先前已经匹配过
                        dp[i][j] = dp[i-1][j]
                    - 此"*"先前未匹配,此时正要匹配第一个字符
                        dp[i][j] = dp[i-1][j-1]
                    - 又因为第二种情况可视为"*"先前匹配了空字符串，因此
                        dp[i][j] = dp[i-1][j]
                所以此情况下:
                    dp[i]dp[j] = dp[i-1][j] or dp[i][j-1]

            - 如果p[j]!="*"：
                - 保证现在可以匹配，即
                    p[j]==s[i] or p[j]=="?"
                - 保证之前可以匹配，即
                    dp[i-1][j-1] == True
        """
        dp = [[False]*(len(p)+1) for i in range(len(s)+1)]
        dp[0][0] = True
        # 考虑长度为0的字符串边界,只有当模式全为"*"时才能匹配成功
        for j in range(len(p)):
            if p[j]=="*":
                dp[0][j+1] = True
            else:
                break

        for i in range(len(s)):
            for j in range(len(p)):
                if p[j]=="*":
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i][j] and (p[j]=="?" or p[j]==s[i])
        # print(dp)
        return dp[-1][-1]