class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub = [[],[],[],[],[],[],[],[],[]]                                    
        for i in range(9):
            se = set()
            for j in range(9):
                if board[i][j]!= ".":
                    if board[i][j] in se:
                        return False
                    se.add(board[i][j])
                    num = int(board[i][j])
                    if i<3:
                        if j<3:
                            sub[0].append(num)
                        elif j<6:
                            sub[1].append(num)
                        elif j<9:
                            sub[2].append(num)
                    elif i<6:
                        if j<3:
                            sub[3].append(num)
                        elif j<6:
                            sub[4].append(num)
                        elif j<9:
                            sub[5].append(num)
                    elif i<9:
                        if j<3:
                            sub[6].append(num)
                        elif j<6:
                            sub[7].append(num)
                        elif j<9:
                            sub[8].append(num) 

        m = len(board[0])
        for i in range(9):
            se = set()
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in se:
                        return False
                    se.add(board[j][i])

        for i in sub:
            se = set()
            for j in i:
                if j in se:
                    return False
                se.add(j)
        return True