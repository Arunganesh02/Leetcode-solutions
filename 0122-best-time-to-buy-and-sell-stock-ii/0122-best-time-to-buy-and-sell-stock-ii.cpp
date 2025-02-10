class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int c = 0;
        int recur = 0;
        while(r<prices.size()){
            int su = prices[r] - prices[l];
            // cout<<su<<" "<<recur<<endl;
            if (prices[l] > prices[r]){
                c += recur;
                l = r;
                r ++ ;
                recur= 0;
            }
            else if (su <= recur){
                c += recur;
                l = r;
                r++;
                recur = 0;
            }
            else{
                recur = su;
                r ++;
            }
        }
        c += recur;
        return c;
    }
};