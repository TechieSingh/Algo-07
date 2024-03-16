// class Solution {
// public:
//     vector<vector<string>> groupAnagrams(vector<string>& strs) {
//         unordered_map<string, vector<string>> m;
//         vector<vector<string>> result;
//         for(const auto& str:strs){
//             string sortedStr {str};
//             ranges::sort(sortedStr);
//             m[sortedStr].push_back(str);
//         }
//         for(auto& [_, x]: m)
//             result.push_back(move(x));
//             return result;
//     }
// };
// Time Complexity: O(n*mlogm), where n is the length of the array and m is the length of the longest string in the array.
// Space Complexity: O(n*m), where n is the length of the array and m is the length of the longest string in the array.