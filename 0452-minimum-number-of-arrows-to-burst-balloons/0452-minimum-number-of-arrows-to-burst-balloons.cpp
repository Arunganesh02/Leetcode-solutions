class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        vector<vector<int>> ans;
        ans.push_back(points[0]);
        for (int i = 1 ; i<points.size();i++){
            if (ans[ans.size()-1][1] >= points[i][0]){
                ans[ans.size()-1][1] = min(ans[ans.size()-1][1] , points[i][1]);
            }
            else{
                ans.push_back(points[i]);
            }

        }
        return ans.size();
    }
};