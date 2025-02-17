# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def traverse(root , su , target , child):
            nonlocal ans
            if not root:
                return
            if root.val + su == target and not root.left and not root.right:
                child.append(root.val)
                ans.append(child)
                return
            child.append(root.val)
            traverse(root.left , su+root.val , target , child[:])
            traverse(root.right , su + root.val , target , child[:])
        traverse(root , 0 , targetSum , [])
        return ans
