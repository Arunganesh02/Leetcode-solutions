class Solution {
public:
    vector<vector<int>> ans ;
    void back(vector<int> li , set<int> se ,vector<int> &nums){
        if(li.size() == nums.size()){
            ans.push_back(li);
            return ;
        }
        for (int i = 0 ; i<nums.size() ; i++){
            if (se.count(i) == 0){
                li.push_back(nums[i]);
                se.insert(i);
                back(li , se , nums);
                li.pop_back();
                se.erase(i);
            }
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        set<int> se;
        back({} , se , nums);
        return ans;
    }
};