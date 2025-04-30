class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        sort(people.begin() , people.end());
        int boats =0;
        int r=people.size()-1 , l = 0;
        while (l<=r){
            if (people[l] + people[r] <= limit){
                boats ++;
                r --;
                l ++;
            }
            else{
                r--;
                boats ++;
            }
        }
        return boats;
    }
};