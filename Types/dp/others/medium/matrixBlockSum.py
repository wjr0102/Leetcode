'''
    1314. 矩阵区域和
'''
class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
            参考滑动窗口

                - 往右移动窗口，则减去最左边一列加上最右边一列
                - 往下移动窗口，则减去最上边一行加上最下边一行
        """
        m,n = len(mat),len(mat[0])
        if K+1>=m and K+1>=n:
            s = 0
            for row in mat:
                s += sum(row)
            ans = [[s for i in range(n)] for j in range(m)]
            return ans
        ans = [[0 for i in range(n)] for j in range(m)]
        # 左上角的框
        s0 = 0
        for i in range(min(m,K+1)):
            for j in range(min(n,K+1)):
                s0 += mat[i][j]
        ans[0][0] = s0
        # 上边界
        si = s0
        l0,r0 = -K-1,K
        for j in range(1,n):
            r0 += 1
            l0 += 1
            # 加新的
            if r0<n:
                for i in range(K+1):
                    si += mat[i][r0]
            # 减旧的
            if l0>=0:
                for i in range(K+1):
                    si -= mat[i][l0]
            ans[0][j] = si

        u0,d0 = -K-1,K
        for i in range(1,m):
            d0 += 1
            u0 += 1
            for k in range(n):
                sj = ans[i-1][k]
                # print(i,k,sj,u0,d0)
                # 加新的
                if d0<m:
                    sj += sum(mat[d0][max(0,k-K):min(n,k+K+1)])
                # 减旧的
                if u0>=0:
                    sj-= sum(mat[u0][max(0,k-K):min(n,k+K+1)])
                ans[i][k] = sj
        return ans

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        """
            二维矩阵前缀和
                - P[i,j]表示以[0,0]为左上角，[i,j]为右下角的矩阵和
                - P[i,j] = P[i-1,j]+P[i,j-1]-P[i-1,j-1]+mat[i,j]
        """
        m, n = len(mat), len(mat[0])
        P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                P[i][j] = P[i - 1][j] + P[i][j - 1] - P[i - 1][j - 1] + mat[i - 1][j - 1]
        
        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return P[x][y]

        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + get(i - K, j - K);
        return ans
