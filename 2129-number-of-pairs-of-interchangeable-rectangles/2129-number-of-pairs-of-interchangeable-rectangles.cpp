class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& rectangles) {
        map<double , long long > mp ;
        long long c = 0;
        for ( auto i : rectangles){
            double nu = (double) i[0] / i[1];
            if (mp.count(nu) ==0){
                mp[nu] = 1;
            }
            else{
                c += mp[nu];
                mp[nu] += 1;
            }
        }
        return c ;
    }
};