#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        // Step 1: Count the frequency of each number
        unordered_map<int, int> freq;
        for (int num : nums) {
            freq[num]++;
        }
        
        // Step 2: Transfer to a vector of pairs
        vector<pair<int, int>> freqPairs;
        for (auto& p : freq) {
            freqPairs.push_back(p);
        }
        
        // Step 3: Sort by frequency ascending, and by value descending if frequencies are the same
        sort(freqPairs.begin(), freqPairs.end(), [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.second == b.second) {
                return a.first > b.first;  // Descending order of values if frequencies are the same
            }
            return a.second < b.second;  // Ascending order of frequencies
        });
        
        // Step 4: Build the result vector based on the sorted frequencies
        vector<int> result;
        for (auto& p : freqPairs) {
            result.insert(result.end(), p.second, p.first);  // Insert 'p.second' copies of 'p.first'
        }
        
        return result;
    }
};
