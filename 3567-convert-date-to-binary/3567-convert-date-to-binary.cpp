class Solution {
public:
    string bin(string da){
        int num = stoi(da);
        string st = "";
        while (num>0){
            int i = num & 1;
            if (i == 1){
                st += '1';
            }
            else{
                st += '0';
            }
            num >>= 1;
        }
        reverse(st.begin() , st.end());
        return st;
    }
    string convertDateToBinary(string date) {
        // return bin("2080");
        string ans = "";
        string temp = "";
        for (int i = 0 ; i<date.size() ; i++){
            if ((char)date[i] != '-'){
                temp += date[i] ;
            }
            else{
                ans += bin(temp);
                ans += "-";
                temp = "";
            }
        }
        ans+= bin(temp);
        return ans;
    }
};