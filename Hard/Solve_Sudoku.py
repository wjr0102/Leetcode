class Solution:
    def solveSudoku(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def getNums(x,y):
            flags = {"1","2","3","4","5","6","7","8","9"}
            # Check row
            for i in range(9):
                if board[x][i] in flags:
                    flags.remove(board[x][i])
            # Check column
            for i in range(9):
                if board[i][y] in flags:
                    flags.remove(board[i][y])
            
            # Firm the block
            R = x // 3
            C = y // 3
            # Check 3X3
            for i in range(3):
                for j in range(3):
                    a = 3*R + i
                    b = 3*C + j
                    if board[a][b] in flags:
                        flags.remove(board[a][b])
            return flags

        def getRows(x):
            rows = set()
            for i in range(9):
                if (x,i) in dic:
                    rows.add((x,i))
            return rows 
        
        def getColumns(y):
            columns = set()
            for i in range(9):
                if (i,y) in dic:
                    columns.add((i,y))
            return columns

        def getBlocks(x,y):
            R = x // 3
            C = y // 3
            blocks = set()

            for i in range(3):
                for j in range(3):
                    a = 3*R + i
                    b = 3*C + j
                    if (a,b) in dic:
                        blocks.add((a,b))
            return blocks


        def updateBox(x,y,val):
            board[x][y] = val
            del(dic[(x,y)])
            return updateBoard(x,y,val)

        def updateBoard(x,y,val):
            rows = getRows(x)
            print(x,y,val)
            print("Rows",end=":")
            print(rows)
            #print(dic.keys())


            # Update row
            for box in rows:
                a = box[0]
                b = box[1]
                if (a,b) in dic and val in dic[(a,b)]:
                    dic[(a,b)].remove(val)
                    print((a,b),dic[a,b],end="\t")
                    if len(dic[(a,b)])==1:
                        v = dic[(a,b)].pop()
                        updateBox(a,b,v)
                    elif len(dic[(a,b)])==0:
                        return False
                        
            columns = getColumns(y)
            print("Columns",end=":")
            print(columns)
            # Update column
            for box in columns:
                a = box[0]
                b = box[1]
                if (a,b) in dic and val in dic[(a,b)]:
                    dic[(a,b)].remove(val)
                    print((a,b),dic[a,b],end="\t")
                    if len(dic[(a,b)])==1:
                        v = dic[(a,b)].pop()
                        updateBox(a,b,v)
                    elif len(dic[(a,b)])==0:
                        return False
            
            blocks = getBlocks(x,y)
            print("Blocks",end=":")
            print(blocks)
            # Update 3X3
            for box in blocks:
                a = box[0]
                b = box[1]
                if (a,b) in dic and val in dic[(a,b)]:
                    dic[(a,b)].remove(val)
                    print((a,b),dic[a,b],end="\t")
                    if len(dic[(a,b)])==1:
                        v = dic[(a,b)].pop()
                        updateBox(a,b,v)
                    elif len(dic[(a,b)])==0:
                        return False
            print()
            return True

        def recoverBox(x,y,val):
            print("recover box")
            print(x,y,val)
            rows = getRows(x)
            columns = getColumns(y)
            blocks = getBlocks(x,y)
            
            for box in rows:
                if box in fills:
                    dic[box] = recovers[box]
                    board[box[0]][box[1]] = "."

            for box in columns:
                if box in fills:
                    dic[box] = recovers[box]
                    board[box[0]][box[1]] = "."
            
            for box in blocks:
                if box in fills:
                    dic[box] = recovers[box]
                    board[box[0]][box[1]] = "."

        def recoverBoard(box,val):
            dic[box] = recovers[box]
            board[box[0]][box[1]] = "."
            recoverBox(box[0],box[1])

        def fillNum():
            print("\033[32m Fill Num \033[0m")
            while dic:
                # print(dic)
                box,pos = dic.popitem()
                recovers[box] = pos.copy()
                while pos:
                    val = pos.pop()
                    print(box,pos,val,len(dic))
                    isOk1 = updateBoard(box[0],box[1],val)
                    if isOk1:
                        print("\033[34m<<<<Fill (%d,%d) with %s is ok\033[0m"%(box[0],box[1],val))
                    else:
                        print("\033[34m>>>>Fail to Fill (%d,%d) with %s is ok\033[0m"%(box[0],box[1],val))
                    isOk2 = fillNum()
                    if not (isOk1 and isOk2):
                        print("\033[33m<<<<Fail!\033[0m")
                        recoverBoard(box,val)
                        return False
                    else:
                        print("\033[33m<<<<Success!\033[0m")
                        return fillNum()
            return True

        dic = {}
        fills = set()
        recovers = {}
        # 填所有唯一确定的数
        print("\033[31m%s \033[0m"%"Only one position.")
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    fills.add((i,j))
                    dic[(i,j)] = getNums(i,j)
                    if len(dic[(i,j)]) == 1:
                        val = dic[(i,j)].pop()
                        updateBox(i,j,val)
        #print(board)
        print("\033[31m%s \033[0m"%"Try")
        fillNum()
        print(board)

if __name__ == "__main__":
    board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
    s = Solution()
    s.solveSudoku(board)