class Solution {
public:
    set<vector<int>> se;

    void traverse(vector<int> li , set<int> seen ,vector<int> nums){
        if ( li.size() == nums.size() ) {
            se.insert(li);
            return ;
        }
        for ( int i = 0 ; i < nums.size() ; i++){
            if ( seen.count(i) == 0){
                vector<int> ne = li;
                ne.push_back(nums[i]);
                set<int> s = seen;
                s.insert(i);
                traverse(ne , s ,nums);
            }
        }
    }
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<int> l ;
        set<int> seti;
        vector<vector<int>> ans;
        traverse(l , seti , nums);
        for(auto i : se){
            ans.push_back(i);
        }
        return ans;
    }
};