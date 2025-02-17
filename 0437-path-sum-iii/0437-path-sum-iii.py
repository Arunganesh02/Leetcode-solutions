# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths = 0
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root : return self.paths
        if root.val == targetSum : 
            self.paths += 1
        def traverse(root, su):
            nonlocal targetSum
            if not root: return 
            if su+root.val == targetSum :
                self.paths += 1
            traverse(root.left , su+root.val)
            traverse(root.right , su+root.val)
        traverse(root.left , root.val)
        traverse(root.right , root.val)
        self.pathSum(root.left , targetSum)
        self.pathSum(root.right , targetSum)
        return self.paths