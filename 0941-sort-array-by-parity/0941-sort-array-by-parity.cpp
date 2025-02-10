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

        int temp = 0 ;
        int count = 0 ;
        int n = nums.size();
        int j  = n-1;
        for ( int i = 0  ; i < j ;){
            int p1= nums[i];
            int p2 = nums[j];
            if (p1%2 != 0  && p2%2 == 0){
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                count ++ ;
                i++;
                j--;
            }
            else if (p1%2!= 0 && p2%2 != 0){
                j --;
            }
            else if (p1%2== 0 && p2%2 == 0){
                i++;
            }
            else{
                j--;
                i++;
            }

        }
        return nums;
        }
    };
