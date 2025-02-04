# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ma = 0
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def finddiff(root, maxi , mini):
            if not root: return 
 
            self.ma = max(self.ma , abs(maxi - root.val) , abs(mini - root.val))    
            finddiff(root.left , max(maxi , root.val) , min(mini , root.val))
            finddiff(root.right ,max(maxi , root.val) , min(mini , root.val))

        finddiff(root.left,root.val , root.val )
        finddiff(root.right,root.val , root.val)
        return self.ma