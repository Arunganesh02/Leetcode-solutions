class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int ma = 0;
        while(r<prices.size()){
            if (prices[r]<prices[l]){
                l = r;
                r ++;
            }
            else{
                int su = prices[r] - prices[l];
                ma = max(ma , su);
                r ++;
            }
        }
        return ma;
    }
};