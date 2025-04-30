class Solution {
public:
    int minSetSize(vector<int>& arr) {
        priority_queue<int> heap;
        map<int,int> mp;
        for(auto i:arr){
            mp[i] = mp[i] + 1;
        }
        for(auto i : mp){
            heap.push(i.second);
        }
        int count =0;
        int half = arr.size()/2;
        int su=arr.size();
        while (!heap.empty()){
            su-= heap.top();
            heap.pop();
            count+= 1;
            if (su <= half){
                break;
            }
        }
        return count;
    }
};