class Solution {
public:
    vector<vector<int>> ans;

    void traverse(vector<int> li , int start , int su , int k ){
        if (su < 0) return ;
        if (su ==0){ 
            if (li.size() == k){
                ans.push_back(li);
                return ;
            }
        }
        for (int i = start ; i < 10 ; i++){
            li.push_back(i);
            traverse(li , i+1 , su - i , k );
            li.pop_back();
        }
    }
    vector<vector<int>> combinationSum3(int k, int n) {
        traverse({} , 1 , n ,k );
        return  ans;
    }
};