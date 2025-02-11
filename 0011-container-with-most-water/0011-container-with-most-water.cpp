class Solution {
public:
    int maxArea(vector<int>& height) {
        int l = 0 , su = 0 , r = height.size()-1;
        while (l<r){
            su = max(su ,min(height[l],height[r]) * (r-l));
            if (height[l] < height[r]) l ++;
            else r--;
        } 
        return su ;  
    }
};