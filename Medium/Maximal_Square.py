'''
    dp
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dp = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))]
        res = 0
        for i in range(len(matrix)):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = 1
        for j in range(len(matrix[0])):
            if matrix[0][j] == "1":
                dp[0][j] = 1
                res = 1
        
        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == "1":
                    if matrix[i-1][j] == "1" and matrix[i][j-1] == "1":
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1]) + 1
                    else:
                        dp[i][j] = 1
                    res = max(res,dp[i][j])
        print(dp)
        return res**2


'''
    暴力法
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        maxLen = 0
        for a in range(len(matrix)):
            for b in range(len(matrix[0])):
                if matrix[a][b]=="0":
                    continue
                #print("ROOT: (%d,%d)"%(a,b))
                # 以此为正方形左上角
                i = a
                j = b
                square = float("inf")
                r,d = len(matrix[0]),len(matrix)
                while i<d and j < r and matrix[i][j] == "1":
                    #print("check (%d,%d)"%(i,j))
                    # Right
                    y = j + 1
                    while y<len(matrix[0]) and matrix[i][y]=="1":
                        y += 1
                    #print("y=%d"%y)
                    # Down
                    x = i + 1
                    while x<len(matrix) and matrix[x][j] == "1":
                        x += 1
                    #print("x=%d"%x)
                    square = min(square,x-a,y-b)
                    d = min(d,a+square)
                    r = min(r,b+square)
                    i += 1
                    j += 1
                    #print("Len: %d\tright: %d\tdown: %d"%(square,r,d))
                    if square < maxLen:
                        break
                square = square - (r-j)
                if square < maxLen:
                    continue
                else:
                    maxLen = square
                #print("maxLen = %d"%maxLen)
        return maxLen**2
                    


