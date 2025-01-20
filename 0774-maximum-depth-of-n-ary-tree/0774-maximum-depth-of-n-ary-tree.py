"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root :
            return 0
        if len(root.children) == 0:
            return 1
        dep = 0
        for i in range(len(root.children)):
            dep = max(dep,self.maxDepth(root.children[i]) + 1)
        return dep