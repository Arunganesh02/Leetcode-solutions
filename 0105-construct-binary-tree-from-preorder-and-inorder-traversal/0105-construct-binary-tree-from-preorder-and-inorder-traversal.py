# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) != 0:
            new = TreeNode(preorder[0])
            head = new
            inde = inorder.index(preorder[0])

            lel = len(inorder[:inde])
            ler = len(inorder[inde+1:])
            if lel and ler:
                head.left = self.buildTree(preorder[1:1+lel] , inorder[:inde])
                head.right = self.buildTree(preorder[1+lel:], inorder[inde+1:])
            elif lel:
                head.left = self.buildTree(preorder[1:1+lel] , inorder[:inde])
            elif ler:
                head.right = self.buildTree(preorder[1+lel:], inorder[inde+1:])
            return head
        else:
            return None