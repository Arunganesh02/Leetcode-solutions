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
public:
    int mini = INT_MAX;
    int pred = INT_MAX;
    int getMinimumDifference(TreeNode* root) {
        if (root){
            getMinimumDifference(root->left);
            int diffi = abs(pred - root->val);
            mini = min(mini, diffi);
            pred = root->val;
            getMinimumDifference(root->right);
        }
        return mini;
    }
};