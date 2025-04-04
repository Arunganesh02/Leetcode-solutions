# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root ):
            if not root.left and not root.right: return (root , 0)
            if not root.left:
                node , dep = traverse(root.right)
                return (node,dep+1)
            elif not root.right:
                node , dep = traverse(root.left)
                return (node,dep+1)
            else:
                nodel , depl = traverse(root.left)
                noder , depr = traverse(root.right)
                if depl == depr: return (root,depl+1)
                elif depl > depr: return (nodel,depl+1)
                else: return (noder,depr+1)
        ans , dep = traverse(root)
        return ans

            