'''
    1140. 石子游戏2

    因为这次规则只取前x堆，所以将1中的[i,j]的状态
    改为[i(从哪开始),M]的状态

    其中s_dp的空间可优化，因为总分数是已知的(游戏1同理)
'''
class Solution:
    def stoneGameII(self, piles) -> int:
        n = len(piles)
        if n<=2:
            return sum(piles)

        # 后缀和
        total = sum(piles)
        suffix = [total]*(len(piles)+1)
        for i in range(1,n+1):
            suffix[i] = suffix[i-1] - piles[i-1]
        print(suffix)
        
        # 初始化
        f_dp = {}
        s_dp = {}
        for i in range(n):
            f_dp[i] = collections.defaultdict(int)
            s_dp[i] = collections.defaultdict(int)

        # 列从后往前填
        for j in range(n-1,-1,-1):
            # 行从下往上填
            for i in range(n-1,-1,-1):
                if 2*(i+1)>=(n-j):
                    f_dp[i][j] = suffix[j]
                else:
                    # 拿走几个
                    for x in range(1,2*(i+1)+1):
                        # 下一个M
                        m = max(i+1,x)-1
                        f_dp[i][j] = max(f_dp[i][j],s_dp[m][j+x]+suffix[j]-suffix[j+x])
                s_dp[i][j] = suffix[j]-f_dp[i][j]
        return f_dp[0][0]