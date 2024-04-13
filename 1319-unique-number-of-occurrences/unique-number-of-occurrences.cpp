class Solution {
public:
    bool uniqueOccurrences(std::vector<int>& arr) {
        std::unordered_map<int, int> mp;
        std::unordered_set<int> freq;

        for (int num : arr) {
            mp[num]++;
        }
        for (const auto& kv : mp) {
            freq.insert(kv.second);
        }
        return freq.size() == mp.size();
    }
};