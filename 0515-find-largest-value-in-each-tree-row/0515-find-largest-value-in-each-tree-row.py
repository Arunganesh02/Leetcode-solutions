# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        que = [root]
        ans = []
        while (len(que) != 0):
            l = len(que)
            ma = float('-inf')
            for i in range(l):
                p = que.pop(0)
                ma = max(ma , p.val)
                if p.left : que.append(p.left)
                if p.right : que.append(p.right)
            ans.append(ma)    
        return ans