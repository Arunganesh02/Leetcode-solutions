class Solution {
public:
    vector<vector<int>> ans;
    void traverse( vector<int> li , set<int> seen , vector<int> &nums){
        if (li.size() == nums.size()){
            ans.push_back(li);
            return ;
        }
        for (int i = 0 ; i<nums.size() ; i++){
            if (seen.count(i) == 0){
                seen.insert(i);
                li.push_back(nums[i]);
                traverse(li , seen , nums);
                li.pop_back();
                seen.erase(i);
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        set<int> seen;
        traverse({} ,seen , nums );
        return ans;
    }
};