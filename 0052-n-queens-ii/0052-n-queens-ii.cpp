class Solution {
public:
bool canplace(vector<vector<string>>& matrix, int i, int j, int n) {
        for (int row = 0; row < i; row++) {
            if (matrix[row][j] =="Q") return false;
        }
        for (int row = i - 1, col = j - 1; row >= 0 && col >= 0; row--, col--) {
            if (matrix[row][col] == "Q") return false;
        }
        for (int row = i - 1, col = j + 1; row >= 0 && col < n; row--, col++) {
            if (matrix[row][col] == "Q") return false;
        }
        return true;
    }
    int back(vector<vector<string>>& matrix , int indi , int n,int& ans){
            if (indi == n ) {
                ans += 1;
                return ans;
            } 
            for(int i = 0 ;i < n;i++){
                if (canplace(matrix ,indi, i , n)){
                    matrix[indi][i] = "Q";
                    back(matrix , indi+1 , n , ans);
                    matrix[indi][i] = ".";
                }
            }
            return ans;
        }

    int totalNQueens(int n) {
        int ans;
        vector<vector<string>> matrix;
        vector<string> temp;
        for(int i = 0 ; i<n; i++){
            temp = {};
            for (int j = 0 ; j<n;j++){
                temp.push_back(".");
            }
            matrix.push_back(temp);
        }
        
        return back(matrix , 0 , n , ans);
        // return ans;
    }
};