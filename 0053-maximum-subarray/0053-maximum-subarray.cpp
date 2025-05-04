class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int ma = INT_MIN;
        int pref = 0 ; 
        for ( int i = 0 ; i<nums.size() ; i++){
            pref = pref + nums[i];
            ma = max(ma , pref);
            if (pref <= 0 ){
                pref = 0;
            }
        }
        return ma;
    }
};