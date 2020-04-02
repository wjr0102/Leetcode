class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        res = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                # top line
                if i-1 >= 0:
                    # left-top
                    if j-1>=0:
                        if board[i-1][j-1]==1:
                            count += 1
                    # top
                    if board[i-1][j]==1:
                        count += 1
                    # right-top
                    if j+1<len(board[0]):
                        if board[i-1][j+1]==1:
                            count += 1
                # same line
                # left
                if j-1>=0:
                    if board[i][j-1]==1:
                        count += 1
                # right
                if j+1 < len(board[0]):
                    if board[i][j+1]==1:
                        count += 1
                # bottom line
                if i+1 < len(board):
                    # left-bottom
                    if j-1 >= 0:
                        if board[i+1][j-1]==1:
                            count += 1
                    # bottom
                    if board[i+1][j]==1:
                        count += 1
                    # right-bottom
                    if j+1 < len(board[0]):
                        if board[i+1][j+1]==1:
                            count += 1
                # check
                if board[i][j]==0 and count==3:
                    res[(i,j)] = 1
                if board[i][j]==1 and (count<2 or count>3):
                    res[(i,j)] = 0
        for key in res:
            board[key[0]][key[1]] = res[key]