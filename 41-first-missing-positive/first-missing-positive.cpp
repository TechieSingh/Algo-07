class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        unordered_map<int,int> mp;
        for(int i=1;i<=nums.size();i++){
            mp[i] = 0;
        }
        for(auto it:nums){
            if(it>0){
                mp[it]++;
            }
        }
        for(int i=1;i<=mp.size();i++){
            if(mp[i] == 0){
                return i;
            }
        }
        return nums.size()+1;
    }
};