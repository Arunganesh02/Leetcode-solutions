class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int maj = 0 , c = 0;
        for (auto i : nums){
            if (maj == i) c++;
            else if ( c == 0) {
                maj = i;
                c = 1;
            }
            else c--;
        }
        return maj;
    }
};