class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0 
        def traverse(i , j ):
            if board[i][j] == ".":
                return 
            

            board[i][j] = '.'
            if j+1 < len(board[0]) and board[i][j+1] == "X":
                traverse(i , j+1)
            elif i+1 < len(board) and board[i+1][j] == "X":
                traverse(i+1 , j)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    traverse(i , j )
                    ans += 1

        return ans
