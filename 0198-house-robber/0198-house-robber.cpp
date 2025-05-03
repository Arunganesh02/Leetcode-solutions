class Solution {
public:
    int traverse(int indi  , vector<int> & nums , vector<int> &dp){

        if (indi <0 ) return 0;
        if (dp[indi] != -1) return dp[indi];
        int nottake = traverse(indi - 1 , nums , dp);
        int take = nums[indi] + traverse(indi - 2 , nums, dp);

        return dp[indi] = max(nottake , take);
    }
    int rob(vector<int>& nums) {
        vector<int> dp(nums.size()  , -1);
        return traverse(nums.size()-1 , nums , dp);
    }
};