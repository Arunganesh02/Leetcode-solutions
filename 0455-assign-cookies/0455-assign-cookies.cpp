class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin() , g.end());
        sort(s.begin(),s.end());
        int gp =0;
        int sp = 0;
        int tot = 0;

        while (gp<g.size() and sp<s.size()){

            if (g[gp] <= s[sp]){
                tot ++ ;
                sp ++;
                gp ++;
            }
            else{
                sp ++;
            }
        }
        return tot; 
    }  
};