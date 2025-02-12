class Solution {
public:
    int sumdigits(int num){
        int ans = 0;
        while (num > 0 ){
            int d= num%10;
            ans += d;
            num /= 10;
        }
        return ans;
    }
    int maximumSum(vector<int>& nums) {
        map < int , int > d;
        int k ;
        int ma = -1;
        for (auto i : nums){
            k = sumdigits(i);
            if (d.count(k)==0){
                d[k] = i;
            }
            else{
                ma = max(ma , d[k] + i);
                d[k] = max(d[k] , i);
            }
        }
        return ma;

    }
};