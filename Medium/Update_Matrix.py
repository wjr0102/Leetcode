class Solution:
    def updateMatrix(self, matrix):
        dp = [[0 for i in range(len(matrix[0]))]for j in range(len(matrix))] 
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    dp[i][j] = float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    ans = dp[i][j]
                    if i-1>=0:
                        ans = min(ans,dp[i-1][j]+1)
                    if j-1>=0:
                        ans = min(ans,dp[i][j-1]+1)
                    dp[i][j] = ans

        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if matrix[i][j] == 1:
                    ans = dp[i][j]
                    if i+1<len(matrix):
                        ans = min(ans,dp[i+1][j]+1)
                    if j+1<len(matrix[0]):
                        ans = min(ans,dp[i][j+1]+1)
                    dp[i][j] = ans
        
        return dp

if __name__ == "__main__":
    print("matrix")
    s = Solution()
    matrix = [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    for i in range(len(matrix)):
        print(matrix[i])
    dp = s.updateMatrix(matrix)
    print("final")
    for i in range(len(dp)):
        print(dp[i])