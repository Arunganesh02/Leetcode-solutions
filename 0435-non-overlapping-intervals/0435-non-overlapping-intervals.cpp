class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end());
        int ans;
        ans= intervals[0][1];
        int rem = 0;
        for(int i =1; i<intervals.size();i++){
            if (intervals[i][0]<ans){
                rem ++;
                ans = min(ans , intervals[i][1]);
            }
            else{
                ans = intervals[i][1];
            }
        }
        return rem;
    }
};