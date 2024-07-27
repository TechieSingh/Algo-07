/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int answer = 0;
    vector<int> dfs(TreeNode* node, int distance) {
        if(node == nullptr) {
            return {};
        }
        if(node->left == nullptr && node->right == nullptr) {
            return {1};
        }
        vector<int> left = dfs(node->left, distance);
        vector<int> right = dfs(node->right, distance);
        
        for(auto l : left) {
            for(auto r : right) {
                if(l + r <= distance) {
                    answer++;
                } 
            }
        }

        vector<int> res;
        for(auto l : left) {
            if(l + 1 < distance) {
                res.push_back(l + 1);
            }
        }
        for(auto r : right) {
            if(r + 1 < distance) {
                res.push_back(r + 1);
            }
        }
        return res;
    }
public:
    int countPairs(TreeNode* root, int distance) {
        dfs(root, distance);
        return answer;
    }
};