class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        priority_queue<long long , vector<long long> , greater<long long>> pq;
        for ( auto i : nums){
            pq.push(i);
        }
        int op = 0;
        long long p , sm1 , sm2; 
        while(true){
            p  = pq.top();
            if (p>=k || pq.size() == 1){
                break;
            }
            sm1 = pq.top();
            pq.pop();
            sm2 = pq.top();
            pq.pop();
            pq.push(min(sm1 , sm2) * 2 + max(sm1 , sm2));
            op ++;
        }
        return op;

    }
};