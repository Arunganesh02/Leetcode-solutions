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
    bool lo = false;
public:
    void addi(TreeNode* root ,int  current , int targetSum){
        if (!root) return ;
        int target = current + root->val;
        if(!root->left && !root->right && target == targetSum){
            lo = true;
        }
        addi(root->left , target , targetSum);
        addi(root->right , target , targetSum);
    }

    bool hasPathSum(TreeNode* root, int targetSum) {
        if (!root) return false;
        if(!root->left && !root->right && root->val == targetSum) return true;
        addi(root->left ,root->val,  targetSum);
        addi(root->right,root->val,targetSum);
        return lo;
    }
};