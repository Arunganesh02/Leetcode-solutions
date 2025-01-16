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
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        if (!root) return {};

        stack<vector<int>> s;
        queue<TreeNode*> que;
        vector<vector<int>> ans;
        TreeNode* node;
        vector<int> ve;
        que.push(root);

        while(!que.empty()){
            int l = que.size();
            ve = {};

            for (int i = 0 ; i<l; i++){
                node = que.front();
                que.pop();

                ve.push_back(node->val);
                if (node->left) que.push(node->left);
                if (node->right) que.push(node->right);
            }
            
            // ans.push_back(ve);  
            s.push(ve);
        }

        while (!s.empty()){
            ans.push_back(s.top());
            s.pop();
        }
        return ans;        
    }
};