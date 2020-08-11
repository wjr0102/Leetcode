'''
    130. 被围绕的区域
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
            多点BFS/DFS
        """
        """
        Do not return anything, modify board in-place instead.
        """
        n =len(board)
        if n<2:
            return
        m = len(board[0])
        if m<2:
            return
        q = []
        # 找边缘O
        # 首行+末行
        for j in range(m):
            if board[0][j]=='O':
                q.append((0,j))
            if board[n-1][j]=='O':
                q.append((n-1,j))
        # 首列+末列
        for i in range(1,n-1):
            if board[i][0]=='O':
                q.append((i,0))
            if board[i][m-1]=='O':
                q.append((i,m-1))
        # DFS
        flags = set()
        DIR = ((0,1),(0,-1),(1,0),(-1,0))
        while q:
            pos = q.pop()
            if pos not in flags:
                flags.add(pos)
                for dirct in DIR:
                    x,y = dirct[0]+pos[0],dirct[1]+pos[1]
                    if 0<=x and x<n and 0<=y and y<m:
                        if board[x][y]=='O':
                            q.append((x,y))
        # 改矩阵
        for i in range(1,n-1):
            for j in range(1,m-1):
                if board[i][j]=='O' and (i,j) not in flags:
                    board[i][j] = 'X'
