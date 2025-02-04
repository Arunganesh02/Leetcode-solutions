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
    int ma = 0 ;
    void diff(TreeNode * root , int maxi , int mini){
        if (!root) return ;
        ma = max(max(ma , abs(maxi - root->val)) , abs(mini - root->val));
        diff(root->left , max(maxi , root->val) , min(mini , root->val));
        diff(root->right , max(maxi , root->val) , min(mini , root->val));
        return ; 
    }
    int maxAncestorDiff(TreeNode* root) {
        diff(root->left , root->val , root->val);
        diff(root->right , root->val , root->val);
        return ma;
    }   
};