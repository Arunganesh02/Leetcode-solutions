# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.li = []
    def dfs(self,node, current):
        if not node:
            return 
        current.append(str(node.val))
        if not node.left and not node.right:
            self.li.append("->".join(current))
            return 
        self.dfs(node.left,current[:])
        self.dfs(node.right,current[:])
        return 
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.dfs(root, [])
        return self.li
            