'''
    718. 最长重复子数组
    找出两个数组最长的公共子数组的长度
'''
class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
            使用动态规划找到长度
            优化: 在暴力求解的基础上，将每个位置需要比较的次数降到了1
            因而将时间复杂度从O(n^3)降到了O(n^2)

            dp思路: 
                对于每一对位置(i,j)做比较:
                    - 如果A[i]==B[j]，则长度为dp[i-1][j-1]+1
                    - 否则，长度为0
        """
        dp = [[0]*len(A) for i in range(len(B))]
        ans = 0
        for i in range(len(A)):
            if B[0]==A[i]:
                dp[i][0] = 1
        for j in range(len(B)):
            if B[j]==A[0]:
                dp[0][j] = 1
        for i in range(1,len(A)):
            for j in range(1,len(B)):
                if B[j]==A[i]:
                    dp[i][j] = dp[i-1][j-1]+1
                    ans = max(ans,dp[i][j])
        # print(dp)
        return ans

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
            滑动窗口
            优化: 之所以多次比较是因为重复的子数组位置没有对齐
            通过对齐位置来减少比较的次数

            对齐的方式:
                - A不动B动
                - B不动A动
        """
        def maxLength(biasA,biasB,length):
            """
                对于每种对齐方式，通过遍历长度length找到最长的子数组长度

                Args:
                    biasA: A数组的初始对齐位置
                    biasB: B数组的初始对齐位置
                    length: 需要遍历的数组长度

                Returns:
                    res: 在此种对齐方式下的最长子数组长度

            """
            res = k = 0
            for i in range(length):
                if A[i+biasA]==B[i+biasB]:
                    k += 1
                    res = max(res,k)
                else:
                    k = 0
            return res

        n,m = len(A),len(B)
        res = 0
        # A不动，每次都从B的第一个元素开始，所以biasB=0
        for i in range(n):
            length = min(n-i,m) # 保证数组不越界
            res = max(res,maxLength(i,0,length))
        # B不动，每次都从A的第一个元素开始，所以biasA=0
        for i in range(m):
            length = min(m-i,n) # 保证数组不越界
            res = max(res,maxLength(0,i,length))
        return res

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
            二分+哈希
            每次二分使用Rabin-Karp算法看是否是子串

            Rabin-Karp算法：
                将字符串转为hash

            本题中，可以将数组看作一个base进制的数，
            则其十进制的值为其哈希值

            tips: 两种转化进制的方式都可以得到正确值
        """
        base, mod = 113, 10**9 + 9

        def hashString(length,S):
            hashS = 0
            for i in range(length):
                hashS += base**(length-i-1)*S[i]
                hashS = hashS % mod
            return hashS

        def hash2(length,S):
            """
                从高位到低位，每低一位就乘以一个base
            """
            hashS = 0
            for i in range(length):
                hashS = (hashS*base+S[i])%mod
            return hashS

        def check(length: int) -> bool:
            hashA = hashString(length,A)
            bucketA = {hashA}
            mult = pow(base, length - 1, mod)
            for i in range(length, len(A)):
                hashA = ((hashA - A[i - length] * mult) * base + A[i]) % mod
                bucketA.add(hashA)
            
            hashB = hashString(length,B)
            if hashB in bucketA:
                return True
            for i in range(length, len(B)):
                hashB = ((hashB - B[i - length] * mult) * base + B[i]) % mod
                if hashB in bucketA:
                    return True

            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        """
            二分+kmp: 待修正
        """
        def get_next(S):
            aNext = [0]*len(S)
            aNext[0] = -1
            for i in range(1,len(S)):
                k = aNext[i-1]
                is_find = False
                while k!=-1 and not is_find:
                    if S[k] == S[i-1]:
                        aNext[i] = aNext[i-1]+1
                        is_find = True
                    else:
                        k = aNext[k]
            return aNext

        def kmp(l,r):
            aNext = get_next(B[l:r+1])
            j = 0
            length = r-l+1
            # print(l,r,aNext)
            while j<len(A)-length+1:
                st1 = j
                for i in range(length):
                    if B[i+l]!=A[i+st1]:
                        if aNext[i]!=-1:
                            j += aNext[i]+1
                        else:
                            j += 1
                        break
                if j==st1:
                    return True
            return False

        def check(length: int) -> bool:
            if length==0:
                return True
            # print("Check %d"%length)
            for i in range(len(B)-length+1):
                if kmp(i,i+length-1):
                    return True
            return False

        left, right = 0, min(len(A), len(B))
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

