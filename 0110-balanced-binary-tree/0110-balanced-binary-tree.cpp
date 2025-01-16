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
    bool lo = true;
public:
    int height(TreeNode * root){
        if(!root) return 0;
        int left = height(root->left);
        int right = height(root->right);
        if(right - left <=1 &&  right - left >=-1){
        }
        else{
            lo =  false;
        };
        return max(left ,right ) +1; 
    }
    bool isBalanced(TreeNode* root) {
        if (!root) return true;
        height(root);
        return lo;
    }
};