class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        // int evec = 0;
        // for (auto i : nums){
        //     if (i%2 == 0){
        //         evec += 1;
        //     }
        // }
        // int ans = 0;
        // for ( int i = 0 ; i < evec;i++){
        //     if (nums[i] % 2 == 1) ans += 1;
        // }
        // return {ans};


        int j;
        for ( int i = 0 , j = 1 ; j < nums.size() && i < nums.size() ;){
            int p1= nums[i];
            int p2 = nums[j];
            if (p1%2 != 0  && p2%2 == 0){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
            else if (p1%2!= 0 && p2%2 != 0){
                j ++;
                continue;
            }
            j++;
            i++;
        }
        return nums;
        }
    };
