# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.li = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.li.append(root.val)
                inorder(root.right)
        inorder(root)
        self.point = 0

    def next(self) -> int:
        ne = self.li[self.point]
        self.point += 1
        return ne

    def hasNext(self) -> bool:
        if self.point+1 <= len(self.li):
            return True
        else:
            return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()