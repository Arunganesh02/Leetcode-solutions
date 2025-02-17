# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        li = []
        def traverse(root , st):
            nonlocal li
            if not root:return 
            if not root.left and not root.right:
                li.append(st+str(root.val))
                return 
            traverse(root.left , st+str(root.val))
            traverse(root.right , st+str(root.val))
        traverse(root, '')
        su = 0
        for i in li:
            su += int(i)
        return su