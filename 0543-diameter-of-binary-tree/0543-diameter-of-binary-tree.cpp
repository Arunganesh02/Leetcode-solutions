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
    int diameter = 0;
public:
    int height(TreeNode* root){
        if (!root) return 0;
        // if (!root->left && !root->right) return 1;
        // cout<<root->val << " ";
        int left , right;
        left =height(root->left) ;
        right = height(root->right);
        diameter = max(diameter , left + right);
        return max(left , right) + 1;
    }
    int diameterOfBinaryTree(TreeNode* root) {
        // diameter = max(diameter , height(root->left) + height(root->right));
        height(root);
        return  diameter;
    }
};