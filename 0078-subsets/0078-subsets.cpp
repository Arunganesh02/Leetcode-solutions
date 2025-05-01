class Solution {
public:
    vector<vector<int>> ans;
    void traverse(vector<int> li , int start , vector<int> &nums ){
        if (start > nums.size()) return ;
        ans.push_back(li);
        for (int i = start ; i<nums.size() ; i++){
            li.push_back(nums[i]);
            traverse(li , i +1 , nums);
            li.pop_back();
        }
        return ;
    }
    vector<vector<int>> subsets(vector<int>& nums) {
        traverse({} , 0 , nums);
        return ans;
    }
};