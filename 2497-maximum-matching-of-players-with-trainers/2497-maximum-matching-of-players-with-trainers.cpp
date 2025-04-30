class Solution {
public:
    int matchPlayersAndTrainers(vector<int>& players, vector<int>& trainers) {
        sort(players.begin() , players.end());
        sort(trainers.begin(),trainers.end());
        int tot=0,pp=0,tp=0;
        while(pp<players.size() && tp<trainers.size()){
            if (players[pp] <= trainers[tp]) { tot++;pp++;tp++;}
            else tp++;
        }
        return tot;
    }
};