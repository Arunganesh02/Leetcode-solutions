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
    bool check(TreeNode *p , TreeNode *q){
        if (!p && q) return false;
        if (p && !q) return false;
        if (p->val == q->val) return true;
        else return false;
    }
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && q) return false;
        if (p && !q) return false;
        if (!p && !q) return true;
        if ((!p->left && !q->left) && (!p->right && !q->right)){
            if  (p->val == q->val) return true;
            else return false;
        }
        bool lol = isSameTree(p->left, q->left);
        bool lor = isSameTree(p->right, q->right); 
        return lol && lor && (p->val == q->val);
    }
};