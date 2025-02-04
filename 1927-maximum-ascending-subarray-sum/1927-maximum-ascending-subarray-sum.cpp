class Solution {
public:
    int maxAscendingSum(vector<int>& nums) {
        int su = nums[0];
        int ma = su;
        for (int i = 1 ; i< nums.size() ; i++){
            if (nums[i]>nums[i-1]){
                su += nums[i];
                ma = max(su , ma);
            }
            else {
                su = 0;
                su += nums[i];
            }
        }
        return ma;
    }
};