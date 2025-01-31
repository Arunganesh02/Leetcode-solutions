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
 #include <climits>
class Solution {
    int mi = INT_MAX;
    int pred = INT_MAX;
public:
    void diffi(TreeNode * root){
        if(root){
            diffi(root->left);
            int diff = abs(pred-root->val);
            mi = min(mi , diff);
            pred = root->val;
            diffi(root->right);
        }
    }
    int minDiffInBST(TreeNode* root) {
        diffi(root);
        return mi;
    }
};