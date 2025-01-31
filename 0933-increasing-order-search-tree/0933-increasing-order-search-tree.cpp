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
    vector<int> ve;

public:
    void inorder(TreeNode* root){
        if(root){
            inorder(root->left);
            ve.push_back(root->val);
            inorder(root->right);
        }

    }
    TreeNode* increasingBST(TreeNode* root) {
        inorder(root);
        TreeNode * head = new TreeNode();
        TreeNode * dumm = head;
        for (int i = 0; i<ve.size();i++){
            head->val = ve[i];
            if (i!=ve.size()-1){
            TreeNode * newi = new TreeNode();
            head->right = newi;
            head  = head->right;
            }

        }
        return dumm;
    }
};