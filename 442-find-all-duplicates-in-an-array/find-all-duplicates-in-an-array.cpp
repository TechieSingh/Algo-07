class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        unordered_map<int,int> mp;
        vector<int> res;
        for(auto d:nums){
            mp[d]++;
        }
        for(auto& co:mp){
            if(co.second>1)
            res.push_back(co.first);
        }
        return res;
    }
};