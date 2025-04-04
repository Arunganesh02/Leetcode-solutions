# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(root):
            if not root.left and not root.right: return (root , 0)
            if not root.right :
                node , dep = traverse(root.left)
                return (node , dep + 1)
            elif not root.left:
                node , dep = traverse(root.right)
                return (node , dep+1)
            else:
                node1 , dep1 = traverse(root.left)
                node2 , dep2 = traverse(root.right)
                if dep1 == dep2: 
                    return (root , dep1 + 1)
                elif dep1 > dep2:
                    return (node1 , dep1 + 1)
                else: return (node2 , dep2 + 1)
        ans , de = traverse(root)
        return ans