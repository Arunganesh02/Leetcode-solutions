class Solution {
public:
    int minStoneSum(vector<int>& piles, int k) {
        priority_queue<double> pq;
        int total = 0;
        for(auto i : piles){
            pq.push(i);
            total += i;
        }
        double p;
        for (int i = 0 ; i<k;i++){
            p = pq.top();
            pq.pop();
            total -= floor(p/2);
            p -= floor(p/2);
            pq.push(p);
        }
        return total;
    }
};