# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0: return
        new = TreeNode(preorder[0])
        if len(preorder)>1:
            inde = postorder.index(preorder[1])
            left = inde
            right = inde+1 
            new.left = self.constructFromPrePost(preorder[1:2+left] , postorder[:left+1])
            new.right = self.constructFromPrePost(preorder[left+2:] , postorder[left+1:len(postorder)-1])
        return new