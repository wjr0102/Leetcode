'''
    97. 交错字符串
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            记忆化递归
        """
        if len(s1)+len(s2)!=len(s3):
            return False

        dic = {}

        def check(p1,p2,p3):
            if (p1,p2,p3) in dic:
                return dic[(p1,p2,p3)]
            # print(p1,p2,p3)
            if p3>=len(s3):
                return True
            if p1<len(s1) and p2<len(s2):
                if s1[p1]!=s3[p3] and s2[p2]!=s3[p3]:
                    return False
            is_ok = False
            if p1<len(s1):
                if s1[p1]==s3[p3]:
                    # print("s1[%d]=s3[%d]"%(p1,p3))
                    is_ok = is_ok or check(p1+1,p2,p3+1)
            if p2<len(s2):
                if s2[p2]==s3[p3]:
                    # print("s2[%d]=s3[%d]"%(p2,p3))
                    is_ok = is_ok or check(p1,p2+1,p3+1)
            dic[(p1,p2,p3)] = is_ok
            return is_ok

        return check(0,0,0)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
            dp
        """
        if len(s1)+len(s2)!=len(s3):
            return False
        dp = [[False]*(len(s2)+1) for i in range(len(s1)+1)]
        dp[0][0] = True
        # 边界
        for i in range(len(s1)):
            # print(i,dp[i])
            dp[i+1][0] = dp[i][0] and (s3[i]==s1[i])
        # print(dp)
        for j in range(len(s2)):
            dp[0][j+1] = dp[0][j] and (s3[j]==s2[j])

        for i in range(len(s1)):
            for j in range(len(s2)):
                dp[i+1][j+1] = (dp[i][j+1] and (s3[i+j+1]==s1[i])) or (dp[i+1][j] and (s3[i+j+1]==s2[j]))

        # print(dp)
        return dp[-1][-1]