class Solution {
public:
    int traverse(int indi , vector<int> & nums ,vector<int> &dp){
        if (indi < 0) return 0;
        if (dp[indi] != -1) return dp[indi];
        return dp[indi] = max(traverse(indi -1  , nums , dp) , nums[indi] + traverse(indi-2 , nums , dp));
    }
    int rob(vector<int>& nums) {
        if (nums.size()==1) return nums[0];

        vector<int> temp1(nums.begin() , nums.end()-1);
        vector<int> dp1(temp1.size() , -1);
        int r1 = traverse(temp1.size()-1 , temp1 , dp1);

        vector<int> temp2(nums.begin() +1 , nums.end());
        vector<int> dp2(temp2.size() , -1);
        int r2 = traverse(temp2.size()-1 , temp2 , dp2);

        return max(r1 , r2);
    }
};