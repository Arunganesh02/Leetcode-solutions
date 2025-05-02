class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board, int row, int col, char dig){
        for(int j=0; j<9; j++){
            if(board[row][j] == dig){
                return false;
            }
        }

        for(int i=0; i<9; i++){
            if(board[i][col] == dig){
                return false;
            }
        }

        int srow = (row/3)*3;
        int scol = (col/3)*3;

        for(int i=srow; i<=srow+2; i++){
            for(int j=scol; j <= scol+2; j++){
                if(board[i][j] == dig) {
                    return false;
                }
            }
        }

        return true;
    }
    bool solve(vector<vector<char>>& board, int i , int j){
        if(i==9) return true;
        if (j == 9) return solve(board , i+1 , 0);
        if (board[i][j] != '.') return solve(board,i,j+1);

        // int co = '1';
        for (char co = '1' ; co<='9'; co++){

            if (isValidSudoku(board , i , j , co)){
                board[i][j] = co;
                if (solve(board , i , j+1)) return true;
                board[i][j] = '.';
            }

        }
        return false;
        // while(j<9){
            // if (board[i][j] == '.'){
            //     board[i][j] = co;
            //     if (!isValidSudoku(board)){
            //         co ++;
            //         if (co>'9') return;
            //         board[i][j] = '.';
            //         continue;
            //     }
            //     else{
            //         if (j+1<9) {
            //             solve(board , i , j+1);
            //         }
            //         else solve(board,i+1, j);
            //         board[i][j] ++;
            //     }
            // }

        }
        
    
    void solveSudoku(vector<vector<char>>& board) {
        solve(board , 0 , 0);
        // return board;
    }
};