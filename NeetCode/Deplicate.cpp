// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         for(int i=0; i<nums.size()-1;i++)
//         {
//             for(int j=i+1; j<nums.size();j++)
//             {
//                 if(nums[i]==nums[j]){
//                     return true;
//                 }
//             }  
//         }
//         return false;
//     }
// };

// The time complexity of this approach is O(n^2), where n is the length of the array.
//this approach is not efficient for large arrays -> TLE

// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         sort(nums.begin(), nums.end());
//         for(int i=0; i<nums.size()-1;i++)
//         {
//                 if(nums[i]==nums[i+1])
//                     return true;       
//         }
//         return false;
//     }
// };
// The time complexity of this approach is O(n log n), where n is the length of the array.

// class Solution {
// public:
//     bool containsDuplicate(vector<int>& nums) {
//         unordered_set<int> seen;
//         for(int num:nums)
//         {
//             if(seen.count(num)>0)
//             return true;

//             else
//             seen.insert(num);
//         }
//         return false;
//     }
// };
// The time complexity of this approach is O(n), where n is the length of the array.