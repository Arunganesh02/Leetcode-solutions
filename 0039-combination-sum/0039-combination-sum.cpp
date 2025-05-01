class Solution {
public:
    vector<vector<int>> ans;
    vector<int> li;
    void traverse(int start  , vector<int>& candidates , int su){
        if (su<0) return ;
        if (su == 0 ){
            ans.push_back(li);
            return ;
        }
        for (int i = start ; i<candidates.size() ; i++){
            li.push_back(candidates[i]);
            traverse(i, candidates , su - candidates[i] );
            li.pop_back();
        }
        return ;
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target){
        traverse(0 , candidates , target);
        return ans;
    }
};