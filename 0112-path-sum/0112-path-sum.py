# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def traverse(root , su):
            nonlocal targetSum
            if not root : return 
            if su + root.val == targetSum and not root.left and not root.right: return True
            return traverse(root.left , su +root.val) or traverse(root.right , su + root.val)
            
        if traverse(root , 0): return True
        else: return False