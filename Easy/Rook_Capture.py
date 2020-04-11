class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # Find Rook
        r_pos = (-1,-1)
        for i in range(8):
            for j in range(8):
                if board[i][j] == 'R':
                    r_pos = (i,j)
                    break
            if r_pos[0]!=-1:
                break
        count = 0
        # Up
        x = r_pos[0] - 1
        while x>=0:
            if board[x][r_pos[1]] == 'B':
                break
            if board[x][r_pos[1]] == 'p':
                count += 1
                break
            x -= 1
        # Down
        x = r_pos[0] + 1
        while x<8:
            if board[x][r_pos[1]] == 'B':
                break
            if board[x][r_pos[1]] == 'p':
                count += 1
                break
            x += 1
        # Left
        y = r_pos[1] - 1
        while y>=0:
            if board[r_pos[0]][y] == 'B':
                break
            if board[r_pos[0]][y] == 'p':
                count += 1
                break
            y -= 1
        # Right
        y = r_pos[1] + 1
        while y<8:
            if board[r_pos[0]][y] == 'B':
                break
            if board[r_pos[0]][y] == 'p':
                count += 1
                break
            y += 1
        return count