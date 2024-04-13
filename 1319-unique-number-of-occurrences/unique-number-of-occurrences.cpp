class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        unordered_map<int, int > mp;
        unordered_map<int, int> freq;
        for(int i =0; i<arr.size();i++){
            mp[arr[i]]++;
        }

        for(auto& co: mp){
            freq[co.second]++;
        }

        for(auto& po: freq){
            if(po.second>1)
            return false;
        }
        return true;
    }
};
