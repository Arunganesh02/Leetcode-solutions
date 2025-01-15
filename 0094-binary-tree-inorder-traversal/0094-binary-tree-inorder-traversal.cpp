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
    vector<int> inorderTraversal(TreeNode* root) {
        if (!root) return ve;
        stack<TreeNode *> sta;
        sta.push(root);
        TreeNode* temp;
        while (!sta.empty()){
            while(root){
                root = root->left;
                if (root) sta.push(root);
            }
            temp = sta.top();
            sta.pop();
            ve.push_back(temp->val);
            if( temp->right){
                sta.push(temp->right);
                root =temp->right;
            }
        }

    return ve;

    }
};