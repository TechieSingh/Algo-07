// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         vector<int> result;
//         for(int i = 0; i < nums.size(); i++) {
//             for(int j = i + 1; j < nums.size(); j++) {
//                 if(nums[i] + nums[j] == target) {
//                     result.push_back(i);
//                     result.push_back(j);
//                     return result;
//                 }
//             }
//         }
//         return result;
//     }
// };
// Time Complexity: O(n^2)
// Space Complexity: O(1)



// class Solution {
// public:
//     vector<int> twoSum(vector<int>& nums, int target) {
//         unordered_map<int, int>m;
//         vector<int> v;
//         for(int i=0; i<nums.size();i++){
//             if(m.count(target-nums[i])){
//                 v.push_back(m[target-nums[i]]);
//                 v.push_back(i);
//                 return v;
//             }
//             m[nums[i]] = i;
//         }
//         return v;
//     }    
// };
// Time Complexity: O(n)
// Space Complexity: O(1)