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
    void insert(TreeNode* root , int val){
        if( val <= root->val){
            if (!root->left){
                TreeNode * newnode = new TreeNode(val);
                root->left = newnode;
                return ;
            }
            else{
                insert(root->left, val);
            }
        }
        else if(val > root->val){
            if(!root->right){
                TreeNode * newnode = new TreeNode(val);
                root->right = newnode;    
                return         ;  
            }
            else{
            insert(root->right,val);
            }
        }
    }
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root){
            TreeNode * newnode = new TreeNode(val);
            root = newnode;
            return root;
        }
        insert(root, val);
        return root;
    }
};