# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        li = []
        def traverse(root):
            nonlocal li
            if root: 
                traverse(root.left)
                li.append(root.val)
                traverse(root.right)
        traverse(root)
        li = sorted(list(set(li)))
        if len(li)<=1:
            return -1
        else:
            return li[1]