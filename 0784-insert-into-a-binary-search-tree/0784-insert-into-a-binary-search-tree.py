# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(root,val):
            if val <= root.val:
                if not root.left:
                    new = TreeNode(val)
                    root.left = new
                    return 
                else:
                    insert(root.left,val)

            elif val > root.val:
                if not root.right:
                    new = TreeNode (val)
                    root.right = new
                else:
                    insert(root.right,val)
        if not root:
            newNode = TreeNode(val)
            root = newNode
            return root
        dum = root
        insert(root,val)
        return dum