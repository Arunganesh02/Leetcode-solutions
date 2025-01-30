# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.d = {}
    def model(self,root):
        if (not root):
            return
        if root.val in self.d:
            self.d[root.val] +=1
        else:
            self.d[root.val] = 1
        self.model(root.left)
        self.model(root.right)
        return 
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.model(root)
        li = sorted(self.d.items() , key = lambda x:x[1])
        ma = li[-1][1]
        ans = []
        for i in self.d:
            if self.d[i] == ma:
                ans.append(i)
        return ans