class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int indi = 0 ;
        for (int i = 0;i<nums.size() ; i++){
            if(nums[i] != val){
                nums[indi] = nums[i];
                indi++;
            }
        }
        return indi;
    }
};