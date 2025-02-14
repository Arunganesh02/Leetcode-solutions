# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        su = 0
        def traverse(root):
            nonlocal su
            if root:
                traverse(root.right)
                root.val = root.val + su
                su = root.val
                traverse(root.left)
        traverse(root)
        return root