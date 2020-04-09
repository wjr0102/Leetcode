class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        dp = {0:[None],1:["()"]}
        for i in range(2,n+1):
            res = []
            for j in range(i):
                # print(i,j)
                left = dp[j]
                right = dp[i-j-1]
                # print("left:%s"%str(left))
                # print("right:%s"%str(right))
                for k1 in left:
                    for k2 in right:
                        if not k1:
                            k1 = ""
                        if not k2:
                            k2 = ""
                        ans = "(" + k1 + ")" + k2
                        if ans not in res:
                            res.append(ans)
                # print(res)
            dp[i] = res[:]
        return dp[n]

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(cur_str,left,right):
            if left==0:
                res.append(cur_str+")"*right)
                return
            if right==0 or left>right:
                return
            dfs(cur_str+"(",left-1,right)
            dfs(cur_str+")",left,right-1)


        dfs("",n,n)
        return res
