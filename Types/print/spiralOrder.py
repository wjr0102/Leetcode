'''
    剑指offer 29. 顺时针打印矩阵
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
            按圈模拟
        """
        if not matrix:
            return []
        row, col = len(matrix),len(matrix[0])
        level = min(row,col) // 2
        res = []
        l,r = -1, col
        u,d = 0, row
        total = row * col
        for k in range(level+1):
            # print("Level %d: l=%d,r=%d,u=%d,d=%d"%(k,l,r,u,d))
            i,j = k,k
            # Right
            while j<r:
                res.append(matrix[i][j])
                j += 1
            if len(res)==total:
                return res
            # Down
            j = r - 1
            i = k + 1
            while i<d:
                res.append(matrix[i][j])
                i += 1
            if len(res)==total:
                return res
            # Left
            i = d - 1
            j = r - 2
            while j>l:
                res.append(matrix[i][j])
                j -= 1
            if len(res)==total:
                return res
            # Up
            j = k
            i = d - 2
            while i>u:
                res.append(matrix[i][j])
                i -= 1
            if len(res)==total:
                return res
            # Update boundary
            l += 1
            r -= 1
            u += 1
            d -= 1
        return res