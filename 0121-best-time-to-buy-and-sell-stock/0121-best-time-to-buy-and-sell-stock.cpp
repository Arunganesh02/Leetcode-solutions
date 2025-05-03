class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1; 
        int ma = 0;
        while (r<prices.size()){
            if (prices[r] < prices[l]) l = r;
            else if ( prices[l] <= prices[r]) ma = max(ma , prices[r]- prices[l]);
            r ++;
        }
        return ma;
    }
};