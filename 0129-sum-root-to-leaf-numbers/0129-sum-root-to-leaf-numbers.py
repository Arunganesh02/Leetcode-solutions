# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        li = 0
        def traverse(root , st):
            nonlocal li
            if not root:return 
            if not root.left and not root.right:
                li += (st*10)+root.val
                return 
            traverse(root.left , (st*10)+root.val)
            traverse(root.right , (st*10)+root.val)

        traverse(root, 0)
        return li