# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if len(postorder) != 0:
            new = TreeNode(postorder[-1])
            inde = inorder.index(postorder[-1])
            
            lenl = len(inorder[:inde])
            lenr = len(inorder[inde+1:])

            if lenl and lenr:
                new.left = self.buildTree( inorder[:inde] , postorder[:lenl])
                new.right = self.buildTree( inorder[inde+1:] , postorder[lenl:lenl+lenr])

            elif lenl:
                new.left = self.buildTree( inorder[:inde] , postorder[:lenl])

            elif lenr:
                new.right = self.buildTree( inorder[inde+1:] , postorder[lenl:lenl+lenr])
            
            return new
        else:
            return None
