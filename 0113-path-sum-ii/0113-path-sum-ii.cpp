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
    vector<vector<int>> ve;
public:
    void addi(TreeNode* root ,int  current , int targetSum , vector<int> nodes){
        if (!root) return ;
        nodes.push_back(root->val);
        if(current+root->val == targetSum && !root->left && !root->right){
            cout<<nodes[0];
            ve.push_back(nodes);
            return ;
        }
        addi(root->left , current + root->val , targetSum , nodes);
        addi(root->right , current + root->val , targetSum , nodes);
    }
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        addi(root , 0 , targetSum , {});
        return ve;
    }
};