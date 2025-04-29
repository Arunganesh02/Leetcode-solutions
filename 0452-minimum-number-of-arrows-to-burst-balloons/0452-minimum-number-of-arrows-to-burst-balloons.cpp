class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        vector<int> ans;
        ans.push_back(points[0][0]);
        ans.push_back(points[0][1]);
        int c = 1;
        for (int i = 1 ; i<points.size();i++){
            if (ans[1] >= points[i][0]){
                ans[1] = min(ans[1] , points[i][1]);
            }
            else{
                // ans.push_back(points[i]);
                ans[0] = points[i][0];
                ans[1] = points[i][1];
                c += 1;
            }

        }
        return c;
    }
};