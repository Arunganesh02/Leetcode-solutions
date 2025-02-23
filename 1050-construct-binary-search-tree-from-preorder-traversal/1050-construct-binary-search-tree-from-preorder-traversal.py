# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        head = None
        def insert(root , value):
            nonlocal head
            if not head:
                head = TreeNode(value)
            else:
                if value > root.val :
                    if not root.right:
                        root.right = TreeNode(value)
                        return 
                    else:
                        insert(root.right , value)
                elif value < root.val:
                    if not root.left: 
                        root.left = TreeNode(value)
                        return 
                    else:
                        insert(root.left , value)
        for i in preorder:
            insert(head , i)
        return head
