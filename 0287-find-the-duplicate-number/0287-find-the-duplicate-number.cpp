class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        // map<int , int > mp;
        // for (auto i : nums){
        //     mp[i] += 1;
        // }
        // for (auto i: mp){
        //     if(i.second > 1) return i.first;
        // }
        // return 0;

        // for (auto i: nums){
        //     if (i<0) i= i*-1;
        //     if (nums[i-1] < 0) return i;
        //     else{
        //         nums[i-1] *= -1;
        //     }
        // }
        // return 0;

        int slow = nums[0];
        int fast = nums[0];
        while (true){
            slow = nums[slow];
            fast = nums[nums[fast]];
            if (slow == fast){
                break;
            }
        }
        int pt = nums[0];
        while(slow != pt){
            slow = nums[slow];
            pt = nums[pt];
        }
        

        return pt;

    }
};